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

from .serializers import UserSerializer
from .models import User
from user_profile.models import Profile
from .utils import check_token

SECRET_FOR_JWT = 'SECRET_KEY'
MESIBO_APPTOKEN = 'q6qk2jt17bu19y0nbscbl7l51g9jfo3gufuoxizctlfhh0fs2ggqolzlr10uf5dh'

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
            return Response({'message': 'already exists'}, status=status.HTTP_400_BAD_REQUEST)
        encoded_url_verification_param = jwt.encode(
            request.data, SECRET_FOR_JWT, algorithm='HS256').decode()
        verification_url = 'http://localhost:8000/user/verify/' + encoded_url_verification_param
        html_message = render_to_string('email_verification.html', {'url_value':verification_url})
        plain_message = strip_tags(html_message)
        subject='Verification for Talentize.ai'
        try:
            send_mail(
                subject,
                plain_message,
                'llr.hall.complaints@gmail.com',
                [request.data['email']],
                html_message=html_message
            )
            return Response({'message': 'success'}, status=status.HTTP_201_CREATED)
        except:
            return Response({'message': 'invalid email'}, status=status.HTTP_400_BAD_REQUEST)


class Login(APIView):
    '''
    Endpoint for login
    '''

    def post(self, request, format=None):
        '''
        function to handle login request
        '''
        password_hash = sha256(request.data['password'].encode()).hexdigest()
        email = request.data['email']
        user = User.objects.filter(email=email, password_hash=password_hash)
        if not len(user):
            return Response({'message': 'invalid creds'}, status=status.HTTP_401_UNAUTHORIZED)
        # change later with actually random string or with SECRET_FOR_JWT
        token = jwt.encode({'email': email, 'random': str(
            datetime.now().timestamp())}, SECRET_FOR_JWT, algorithm='HS256').decode()
        return Response({'token': token, 'message': 'success'}, status=status.HTTP_202_ACCEPTED)


class Verify(APIView):
    '''
    Endpoint to verify user email for signing up
    '''

    def get(self, request, hashed_code, format=None):
        '''
        function to handle GET request 
            verifies email and stores user in DB
        '''
        user_data = jwt.decode(hashed_code.encode(),
                               SECRET_FOR_JWT, algorithms=['HS256'])
        serializer = UserSerializer(data=user_data)
        if serializer.is_valid():
            original_password = user_data['password_hash']
            password_hash = sha256(original_password.encode()).hexdigest()
            # Obtain mesibo access token
            data = {
                "op": "useradd",
                "token": MESIBO_APPTOKEN,
                "addr": user_data['email'],
                "appid": "8117"
            }
            res = requests.post('https://api.mesibo.com/api.php', data=data)
            mesibo_uid = res.json()['user']['uid']
            mesibo_token = res.json()['user']['token']
            serializer.save(password_hash=password_hash, mesibo_uid=mesibo_uid, mesibo_token=mesibo_token,profile=Profile())
            return Response({'message': 'success'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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
        except:
            return Response({'message': 'Invalid user'}, status=status.HTTP_400_BAD_REQUEST)
