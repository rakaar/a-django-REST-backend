from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from user.utils import check_token


class Profile(APIView):
    '''
    GET endpoint to get/retrive profile details
    '''

    def get(self, request, format=None):
        email = request.data['email']
        if not check_token(email, request.data['token']):
            return Response({'message': 'token validation failed'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            user = User.objects.filter(email=email)[0]
        except User.DoesNotExist:
            return Response({'message': 'Invalid User'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            profile = user.profile
            return Response(profile, status=status.HTTP_200_OK)
