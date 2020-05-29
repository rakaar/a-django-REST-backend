from django.shortcuts import render

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

import requests

from user.utils import MESIBO_APPTOKEN, MESIBO_APP_ID
from .models import Group

class MesiboGroup(APIView):
    '''
    Endpoint to manage groups
    '''

    def post(self, request, format=None):
        '''
        Create a new chat group
        '''
        data = request.data
        data['op'] = 'groupadd'
        data['token'] = MESIBO_APPTOKEN
        try:
            response = request.post('https://api.mesibo.com/api.php', data=data)
            gid = response.json()['group']['gid']
            name = data['name']
            group = Group(gid=gid, name=name)
            group.save()
            return Response({ 'message': 'success', 'gid': gid, 'name': name}, status=status.HTTP_200_OK)
        except:
            return Response({ 'message': 'failure' }, status=status.HTTP_400_BAD_REQUEST)


    def get(self, request, format=None):
        '''
        To get users of a group
        '''
        try:
            gid = request.data['gid']
            groups = Group.objects.filter(gid=gid)
            users = [x.email for x in groups]
            return Response({'users': users}, status=status.HTTP_200_OK)
        except:
            return Response({'message': 'not found'}, status=status.HTTP_400_BAD_REQUEST)


