from django.core.mail import send_mail
from django.contrib.auth.hashers import make_password
from django.contrib.auth.base_user import BaseUserManager

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from hashlib import sha256
import jwt
import requests
import json
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
        print(encoded_url_verification_param)
        verification_url = 'localhost:8000/user/verify/' + encoded_url_verification_param
        send_mail(
            'Subject here',
            verification_url,
            'llr.hall.complaints@gmail.com',
            [ request.data['email'] ],
        )
        return Response({'message': 'success'}, status=status.HTTP_201_CREATED)


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
        secret = 'RANDOMLY_GENERATED_SECURE_STRING_BY_KAU' # change later with actually random string or with SECRET_FOR_JWT
        token = jwt.encode({'email': email, 'random': str(
            datetime.now().timestamp())}, secret, algorithm='HS256').decode()
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
    POST to send access token from Google OAuth
    PUT to update details of user
    '''
    def post(self, request, format=None):
        payload = {'access_token': request.data.get("token")}  
        r = requests.get('https://www.googleapis.com/oauth2/v2/userinfo', params=payload)
        data = json.loads(r.text)

        if 'error' in data:
            return Response({'message': 'wrong or expired google token'}, status=status.HTTP_401_UNAUTHORIZED)

        try:
            user = User.objects.filter(email=data['email'])
            message = 'success'
        except User.DoesNotExist:
            user = User()
            user.email = data['email']
            user.password_hash = make_password(BaseUserManager().make_random_password())
            user.save()
            message = 'new user'
            
        token = jwt.encode({'email': data['email'], 'random': str(
            datetime.now().timestamp())}, SECRET_FOR_JWT, algorithm='HS256').decode()
        return Response({'token': token, 'message': message }, status=status.HTTP_202_ACCEPTED)


    def put(self, request, format=None):
        email = request.data['email']
        token = request.data['token']
        is_valid_token = check_token(email, token)
        if is_valid_token:
            return Response({ 'message': 'success'}, status=status.HTTP_200_OK)
        else:
            return Response({ 'message': 'invalid token'}, status=status.HTTP_401_UNAUTHORIZED)        