from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.contrib.auth.hashers import make_password
from django.contrib.auth.base_user import BaseUserManager
from django.shortcuts import render

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from hashlib import sha256
import jwt
import requests
import json
import base64
from datetime import datetime
from logging import getLogger

from .serializers import UserSerializer
from .models import User, LastSeen, MesiboUser
from chat.models import Group, Mail
from user_profile.models import Profile
from .utils import check_token, is_token_valid, MESIBO_APP_ID, MESIBO_APPTOKEN
from .utils import SECRET_KEY_FOR_JWT as SECRET_FOR_JWT
logger = getLogger(__name__)


class Signup(APIView):
    '''
    Endpoint for signup
    '''

    def post(self, request, format=None):
        '''
        function to handle signup 
            send verification email to user
        '''
        already_exists = User.objects.filter(email=request.data['email'])
        if already_exists:
            return Response({'message': 'already exists'}, status=status.HTTP_409_CONFLICT)
        encoded_url_verification_param = jwt.encode(
            request.data, SECRET_FOR_JWT, algorithm='HS256').decode()
        verification_url = 'http://localhost:3000/user/verify/' + \
            encoded_url_verification_param
        html_message = render_to_string('email_verification.html', {
                                        'url_value': verification_url})
        plain_message = strip_tags(html_message)
        subject = 'Verification for Talentize.ai'
        try:
            send_mail(
                subject,
                plain_message,
                'llr.hall.complaints@gmail.com',
                [request.data['email']],
                html_message=html_message
            )
            return Response({'message': 'success'}, status=status.HTTP_201_CREATED)
        except Exception as e:
            logger.error('Error in SignUp POST is ', e)
            return Response({'message': 'invalid email'}, status=status.HTTP_400_BAD_REQUEST)


class Login(APIView):
    '''
    Endpoint for login
    '''

    def post(self, request, format=None):
        '''
        function to handle login request
        '''
        print('LOGIN DATA :', request.data)
        password_hash = sha256(request.data['password'].encode()).hexdigest()
        email = request.data['email']
        user = User.objects.filter(email=email, password_hash=password_hash)
        if not len(user):
            return Response({'message': 'invalid creds'}, status=status.HTTP_401_UNAUTHORIZED)
        token = jwt.encode({'email': email, 'random': str(
            datetime.now().timestamp())}, SECRET_FOR_JWT, algorithm='HS256').decode()
        return Response({'token': token, 'message': 'success'}, status=status.HTTP_200_OK)


class Verify(APIView):
    '''
    Endpoint to verify user email for signing up
    '''

    def get(self, request, hashed_code, format=None):
        '''
        function to handle GET request 
            verifies email and stores user in DB
        '''
        try:
            user_data = jwt.decode(hashed_code.encode(),
                                SECRET_FOR_JWT, algorithms=['HS256'])
            original_password = user_data['password_hash']
            password_hash = sha256(original_password.encode()).hexdigest()
            # Obtain mesibo access token
            data = {
                "op": "useradd",
                "token": MESIBO_APPTOKEN,
                "addr": user_data['email'],
                "appid": MESIBO_APP_ID
            }
        except Exception as e:
            logger.error('Error in Verify GET is ', e)
            return Response({'message':'data error'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            res = requests.post('https://api.mesibo.com/api.php', data=data)
        except Exception as e:
            logger.error('Error in Verify GET is ', e)
            return Response({'message':'mesibo failure'}, status=status.HTTP_503_SERVICE_UNAVAILABLE)
        mesibo_uid = res.json()['user']['uid']
        mesibo_token = res.json()['user']['token']
        try:
            user = User(name=user_data['name'],email=user_data['email'], password_hash=password_hash, insti_email=user_data['insti_email'], mesibo_details=MesiboUser(uid=mesibo_uid,
                            access_token=mesibo_token), profile=Profile())
            user.save()
            return Response({'message': 'success'}, status=status.HTTP_201_CREATED)
        except Exception as e:
            logger.error('Error in Verify GET is ', e)
            return Response({'message':'db failure'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ForgotPassword(APIView):
    '''
    Endpoint for forget password
    '''

    def post(self, request, format=None):
        '''
        function to handle POST request to set new password
        '''
        email = request.data['email']
        if activity == "forgot":
            try:
                user = User.objects.get(email=email)
            except Exception as e:
                logger.error('Not found user: ', email, ' err: ', e)
                return Response({'message': 'not found'}, status=status.HTTP_400_BAD_REQUEST)

            try:
                token = jwt.encode({'email': email, 'random': str(
                    datetime.now().timestamp())}, SECRET_FOR_JWT, algorithm='HS256').decode()
                send_mail(
                    'Password Reset for Talentize',
                    'Here is a URL - Frotnend.com/forget/' + token,
                    'llr.hall.complaints@gmail.com',
                    [request.data['email']],
                    html_message=html_message
                )
                return Response({'message': 'success'}, status=status.HTTP_201_CREATED)
            except Exception as e:
                logger.error('Error in SignUp POST is ', e)
                return Response({'message': 'invalid email'}, status=status.HTTP_400_BAD_REQUEST)

        elif activity == "update":
            token = request.data['token']
            email = jwt.decode(token, SECRET_KEY_FOR_JWT,
                               algorithms=['HS256'])['email']
            new_password = request.data['password']
            if not is_token_valid(token):
                return Response({'message': 'token expired'}, status=status.HTTP_400_BAD_REQUEST)
            try:
                user = User.objects.get(email=email)
                user.password_hash = sha256(new_password.encode()).hexdigest()
                user.save()
                return Response({'message': 'success'}, status=status.HTTP_200_OK)
            except Exception as e:
                logger.error('Error in forget password is ', e)
                return Response({'message': 'failure'}, status=status.HTTP_400_BAD_REQUEST)


class ResetPassword(APIView):
    '''
    Endpoint to reset a user's password
    '''

    def post(self, request, format=None):
        '''
        function to handle POST request to update password
        '''
        data = request.data
        if data['activity'] == 'token':
            if check_token(data['email'], data['token']):
                token = jwt.encode({'email': data['email'], 'random': str(
                    datetime.now().timestamp())}, SECRET_FOR_JWT, algorithm='HS256').decode()
                return Response({'message': 'success'}, status=status.HTTP_200_OK)
            else:
                return Response({'message': 'invalid token'}, status=status.HTTP_400_BAD_REQUEST)
        elif data['activity'] == 'update':
            password_hash = sha256(data['password'].encode()).hexdigest()
            user = User.objects.get(email=data['email'])
            if user.password_hash == password_hash:
                if is_token_valid(data['token']):
                    new_password_hash = sha256(
                        data['new_password'].encode()).hexdigest()
                    user.password_hash = new_password_hash
                    user.save()
                    return Response({'message': 'success'}, status=status.HTTP_200_OK)
                return Response({'message': 'invalid token'}, status=status.HTTP_400_BAD_REQUEST)
            return Response({'message': 'incorrect password'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({'message': 'invalid activity'}, status=status.HTTP_400_BAD_REQUEST)


class GoogleOAuth(APIView):
    '''
    Endpoint to send authorization code from Google OAuth via client
    '''

    def post(self, request, format=None):
        '''
        function to handle POST request for Google Oauth
        '''
        # Tasks left
        # Fetching authorization code from frontend
        # Using the above to send to Google  to get Access token
        payload = {'access_token': request.data.get("token")}
        r = requests.get(
            'https://www.googleapis.com/oauth2/v2/userinfo', params=payload)
        data = json.loads(r.text)

        if 'error' in data:
            return Response({'message': 'wrong or expired google token'}, status=status.HTTP_401_UNAUTHORIZED)

        try:
            user = User.objects.filter(email=data['email'])
            message = 'success'
        except User.DoesNotExist:
            user = User()
            user.name = data['name']
            user.email = data['email']
            user.password_hash = make_password(
                BaseUserManager().make_random_password())
            user.save()
            message = 'new user'

        token = jwt.encode({'email': data['email'], 'random': str(
            datetime.now().timestamp())}, SECRET_FOR_JWT, algorithm='HS256').decode()
        return Response({'token': token, 'message': message, 'name': data['name'], 'email': data['email']}, status=status.HTTP_202_ACCEPTED)


class LinkedinOAuth(APIView):
    '''
    Endpoint to send authorization code from LinkedIn Oauth via client
    '''

    def post(self, request, format=None):
        '''
        function to handle POST request for Linkedin Oauth
        '''
        # Tasks left:
        # Fetching authorization code in frontend from linkedin
        #  Fetching authorization token from frontend in request.data['auth_code']- 3 lines below this
        payload_for_token = {
            'grant_type': 'code',
            'code': request.data['auth_code'],
            'redirect_uri': 'frontend.com/profile',
            'client_id': 'CLIENT_ID_FROM_LINEKDIN DEV',
            'client_secret': 'FROM LINEKDIN DEV'
        }
        response_for_token = requests.post(
            'https://www.linkedin.com/oauth/v2/accessToken', data=payload_for_token)
        response_for_token = json.loads(response_for_token.text)
        access_token = response_for_token['access_token']

        try:
            response_for_data = requests.get(
                'https://api.linkedin.com/v2/me/~format=json?oauth2_access_token='+access_token)
            response_for_data = json.loads(response_for_data.text)
        except:
            return Response({'message': 'cant connect to linkedin API'}, status=status.HTTP_401_UNAUTHORIZED)

        email = response_for_data['email']
        try:
            user = User.objects.filter(email=data['email'])
            message = 'success'
        except User.DoesNotExist:
            user = User()
            user.name = data['name']
            user.email = data['email']
            user.password_hash = make_password(
                BaseUserManager().make_random_password())
            user.save()
            message = 'new user'

        token = jwt.encode({'email': response_for_data['email'], 'random': str(
            datetime.now().timestamp())}, SECRET_FOR_JWT, algorithm='HS256').decode()
        return Response({'token': token, 'message': message, 'name': response_for_data['name'], 'email': response_for_data['email']}, status=status.HTTP_202_ACCEPTED)


class AppleOAuth(APIView):
    '''
    Endpoint to listen to redirect repsonse from Apple
    '''

    def post(self, request, format=None):
        '''
        function to handle
            POST request from apple upon authentication
        '''
        id_token = request.data['id_token']
        encoded_data = id_token.split('.')[1]
        user_data = base64.b64decode(encoded_data).decode()
        sub = json.loads(user_data)['sub']

        try:
            user = User.objects.filter(password_hash=sub)
        except User.DoesNotExist:
            user = User()
            data_from_apple = request.data['user']
            user.name = data_from_apple['name']['firstName'] + \
                ' ' + data_from_apple['name']['lastName']
            user.email = data_from_apple['email']
            user.password_hash = sub
            user.save()
        return (request, 'user/go_to_profile.html', {'sub': sub})
        # button onclick => window.location.href = frontend.com/user/apple/sub/is_new_user


class AppleUserToProfile(APIView):
    '''
    Endpoint to handle redirect to profile page after apple authentication
    '''

    def post(self, request, sub, format=None):
        '''
        function to handle
            POST request sent from frontend with data - sub
        '''
        try:
            user = User.objects.filter(password_hash=sub)
            token = jwt.encode({'email': user.email, 'random': str(
                datetime.now().timestamp())}, SECRET_FOR_JWT, algorithm='HS256').decode()
            return Response({'message': 'success', 'token': token}, status=status.HTTP_200_OK)
        except Exception as e:
            logger.error('Error in AppleUserToProfile POST is ', e)
            return Response({'message': 'Invalid user'}, status=status.HTTP_400_BAD_REQUEST)


class ReadBy(APIView):
    '''
    Endpoint to handle readby for messages in a group
    '''

    def get(self, request, format=None):
        '''
        function to return list of users seen/unseen info
        '''
        data = request.data
        uid = data['uid']
        gid = data['gid']
        mid = data['mid']
        try:
            user = User.objects.get(email=uid)
            for group in user.mesibo_details.groups:
                if gid == group.gid:
                    for message in group.last_seen_msgs:
                        if mid == message.mid:
                            flag, uids = message.flag, message.uni_ids
            u_names = []
            if flag == 'read':
                for a_uid in uids:
                    a_user = User.objects.get(email=a_uid.email)
                    u_names.append(a_user.name)
            else:
                members = Group.objects.get(gid).uni_ids
                members_who_read = [
                    member.email for member in members if member not in uids]
                for a_uid in members_who_read:
                    a_user = User.objects.get(email=a_uid)
                    u_names.append(a_user.name)

            return Response({'read_by': u_names}, status=status.HTTP_200_OK)
        except Exception as e:
            logger.error('Error in ReadBy GET is ', e)
            return Response({'message': 'not found'}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, format=None):
        '''
        Endpoint to store people who read the last 5 messages of user
        '''

        uid = request.data['uid']
        uid_reader = request.data['uid_reader']
        gid = request.data['gid']
        mid = request.data['mid']

        try:
            user = User.objects.get(email=uid)
            user_group = [
                group for group in user.mesibo_details.groups if group.gid == gid][0]
            mesibo_group = Group.objects.get(gid=gid)
            max_num_readers = int(len(mesibo_group.uni_ids)/2)
            last_seen_msg_ids = [msg.mid for msg in group.last_seen_msgs]

            # If a new message comes in
            if mid not in last_seen_msg_ids:
                if len(user_group.last_seen_msgs) == 5:
                    user_group.last_seen_msgs.pop(0)
                    user.save()
                lastseen = LastSeen(mid=mid, flag='read', uni_ids=[
                                    Mail(email=uid_reader)])
                user_group.last_seen_msgs.append(lastseen)
                user.save()
                return Response({'message': 'success'}, status=status.HTTP_200_OK)

            # For an already existing message
            last_seen_msg = [
                last_seen_msg for last_seen_msg in group.last_seen_msgs if last_seen_msg.mid == mid][0]
            if last_seen_msg.flag == 'read':
                if len(last_seen_msg.uni_ids) < max_num_readers:
                    last_seen_msg.uni_ids.append(Mail(email=uid_reader))
                    user.save()
                    return Response({'message': 'success'}, status=status.HTTP_200_OK)
                # If limit exceeds, flag becomes unread and contains all un_read users
                else:
                    last_seen_msg.flag = 'unread'
                    all_emails = [
                        email for uni_id.email in mesibo_group.uni_ids]
                    readers = [
                        uni_id.email for uni_id in user_group.last_seen_msgs.uni_ids]
                    readers.append(uid_reader)
                    un_read = [
                        mail for mail in all_emails if mail not in readers]
                    un_read_objs = [Mail(email=email) for email in un_read]
                    last_seen_msg.uni_ids = un_read_objs
                    user.save()
                    return Response({'message': 'success'}, status=status.HTTP_200_OK)

            elif last_seen_msg.flag == 'unread':
                # check if the user is in unread, because it might happen that user joined the group late
                unread_emails = [
                    uni_id.email for uni_id in last_seen_msg.uni_ids]
                if uid_reader in unread_emails:
                    index = [idx for idx, element in enumerate(
                        last_seen_msg.uni_ids) if element.email == uid_reader][0]
                    last_seen_msgs.uni_ids.pop(index)
                    return Response({'message': 'suceess'}, status=status.HTTP_200_OK)
                else:
                    return Response({'message': 'suceess'}, status=status.HTTP_200_OK)

        except Exception as e:
            logger.error('Error in ReadBy POST is ', e)
            return Response({'message': 'error'}, status=status.HTTP_400_BAD_REQUEST)
