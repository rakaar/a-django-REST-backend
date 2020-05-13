from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from hashlib import sha256

from .serializers import UserSerializer
from .models import User


class HandleUser(APIView):
    '''
    Return list of all users if GET, Save a new user if POST
    '''
    def get(self, request, format=None):
        all_users = User.objects.all()
        serializer = UserSerializer(all_users, many=True)
        return Response(serializer.data)

    def post(self, request, format = None):
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
        is_already_exists = User.objects.filter(email=request.data['email'])   #check if user already registered by same mail
        if is_already_exists:
            return Response({ 'message': 'already exists'}, status=status.HTTP_400_BAD_REQUEST)
            
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            original_password = request.data['password_hash']
            password_hash = sha256(original_password.encode()).hexdigest()   # save password hash instead of the password
            serializer.save(password_hash=password_hash)
            ## PANKAJ serializer.data is the data which contains in json format, like these 
                #{
                #     "name": "kkk",
                #     "email": "kksssssssss@m.com",
                #     "insti_email": "jjfjf@m.com",
                #     "password_hash": "52f104d3b9597c6a52693d75c1bfdd7a446e87c6f87793240fa7b7574ffe1cc9"
                # }
            # SEND MAIL HERE

            # END CODE
            # DELTE THIS USELESS COMMENTs LATER
            
            return Response({ 'message': 'success'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Login(APIView):
    '''
    POST Endpoint for login
    '''
    def post(self, request, format=None):
        print(request.data)
