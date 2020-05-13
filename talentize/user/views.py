from django.core.mail import send_mail
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from hashlib import sha256
import jwt
from datetime import datetime
# from simplecrypt import encrypt

from .serializers import UserSerializer
from .models import User
import jwt


class HandleUser(APIView):
    '''
    Return list of all users if GET, Save a new user if POST
    '''

    def get(self, request, format=None):
        all_users = User.objects.all()
        serializer = UserSerializer(all_users, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():

            print('HASH is ', password_hash)
            print('HERE')
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Signup(APIView):
    '''
    POST Endpoint for signup
    '''

    def post(self, request, format=None):
        # check if user already registered by same mail
        is_already_exists = User.objects.filter(email=request.data['email'])
        if is_already_exists:
            return Response({'message': 'already exists'}, status=status.HTTP_400_BAD_REQUEST)

        # can change 'rakaar_ki_jai' with anything or can let it be
        encoded_url_verification_param = jwt.encode(
            request.data, 'rakaar_ki_jai', algorithm='HS256').decode()
        print(encoded_url_verification_param)
        verification_url = 'localhost:8000/user/verify/' + encoded_url_verification_param
        send_mail(
            'Subject here',
            'Here is the message :' + verification_url,
            'llr.hall.complaints@gmail.com',
            ['rka87338@gmail.com'],

        )

        # PANKAJ serializer.data is the data which contains in json format, like these
        # {
        #     "name": "kkk",
        #     "email": "kksssssssss@m.com",
        #     "insti_email": "jjfjf@m.com",
        #     "password_hash": "52f104d3b9597c6a52693d75c1bfdd7a446e87c6f87793240fa7b7574ffe1cc9"
        # }
        # SEND MAIL HERE

        # END CODE
        # DELTE THIS USELESS COMMENTs LATER

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
        secret = 'RANDOMLY_GENERATED_SECURE_STRING_BY_KAU'
        token = jwt.encode({'email': email, 'random': str(
            datetime.now().timestamp())}, secret, algorithm='HS256').decode()
        return Response({'token': token, 'message': 'success'}, status=status.HTTP_202_ACCEPTED)


class Verify(APIView):
    '''
    GET endpoint to verify email
    '''

    def get(self, request, hashed_code, format=None):
        user_data = jwt.decode(hashed_code.encode(),
                               'rakaar_ki_jai', algorithms=['HS256'])
        serializer = UserSerializer(data=user_data)
        if serializer.is_valid():
            original_password = request.data['password_hash']
            # save password hash instead of the password
            password_hash = sha256(original_password.encode()).hexdigest()
            serializer.save(password_hash=password_hash)
            return Response({'message': 'success'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
