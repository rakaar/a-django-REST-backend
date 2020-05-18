from django.core.mail import send_mail
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
from .utils import check_token

SECRET_FOR_JWT = 'SECRET_KEY'


class Signup(APIView):
    '''
    POST Endpoint for signup
    '''

    def post(self, request, format=None):
        already_exists = User.objects.filter(email=request.data['email'])
        if already_exists:
            return Response({'message': 'already exists'}, status=status.HTTP_400_BAD_REQUEST)
        encoded_url_verification_param = jwt.encode(
            request.data, SECRET_FOR_JWT, algorithm='HS256').decode()
        verification_url = 'localhost:8000/user/verify/' + encoded_url_verification_param
        try:
            send_mail(
                'Subject here',
                verification_url,
                'llr.hall.complaints@gmail.com',
                [request.data['email']],
            )
            return Response({'message': 'success'}, status=status.HTTP_201_CREATED)
        except:
            return Response({'message': 'invalid email'}, status=status.HTTP_400_BAD_REQUEST)


class Login(APIView):
    '''
    POST Endpoint for login
    '''

    def post(self, request, format=None):
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
    GET endpoint to verify email
    '''

    def get(self, request, hashed_code, format=None):
        user_data = jwt.decode(hashed_code.encode(),
                               SECRET_FOR_JWT, algorithms=['HS256'])
        serializer = UserSerializer(data=user_data)
        if serializer.is_valid():
            original_password = user_data['password_hash']
            password_hash = sha256(original_password.encode()).hexdigest()
            serializer.save(password_hash=password_hash)
            return Response({'message': 'success'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GoogleOAuth(APIView):
    '''
    POST to send authorization code from Google OAuth via client
    '''

    def post(self, request, format=None):
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
    POST end point to send authorization code from LinkedIn Oauth via client
    '''

    def post(self, request, format=None):
        # Tasks left:
        # Fetching authorization code in frontend from linkedin
        #  Fetching authorization token from frontend in request.data['auth_code'] - line 121
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
    POST endpoint to listen to redirect repsonse from Apple
    '''
    
    def post(self, request, format=None):
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
        return (request, 'user/go_to_profile.html', { 'sub': sub })
        # button onclick => window.location.href = frontend.com/user/apple/sub/is_new_user
    
        

class AppleUserToProfile(APIView):
    '''
    POST request sent from frontend with data - sub
    '''

    def post(self, request, sub, format=None):
        try:
            user = User.objects.filter(password_hash=sub)
            token = jwt.encode({'email': user.email, 'random': str(
                datetime.now().timestamp())}, SECRET_FOR_JWT, algorithm='HS256').decode()
            return Response({'message': 'success', 'token': token}, status=status.HTTP_200_OK)
        except:
            return Response({'message': 'Invalid user'}, status=status.HTTP_400_BAD_REQUEST)
