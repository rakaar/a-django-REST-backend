from django.shortcuts import render

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

import requests

from user.utils import MESIBO_APPTOKEN, MESIBO_APP_ID
from .models import Group, Mail

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
        data['flag'] = 0
        data['active'] = 1
        try:
            response = requests.post('https://api.mesibo.com/api.php', data=data)
            gid = response.json()['group']['gid']
            name = data['name']
            group = Group(gid=gid, name=name)
            group.save()
            return Response({ 'message': 'success', 'gid': gid, 'name': name}, status=status.HTTP_200_OK)
        except Exception as e:
            print('excpetion is ',e)
            return Response({ 'message': 'failure' }, status=status.HTTP_400_BAD_REQUEST)


    def get(self, request, gid, format=None):
        '''
        To get users of a group
        '''
        try:
            gid = request.data['gid']
            print('gid is ',gid)
            group= Group.objects.filter(gid=gid)
            users = [x.uni_ids for x in group]
            return Response({'users': users}, status=status.HTTP_200_OK)
        except Exception as e:
            print('issue is ',e)
            return Response({'message': 'not found'}, status=status.HTTP_400_BAD_REQUEST)



class MesiboUser(APIView):
    '''
    Endpoints to handle user operations related to group
    '''
    
    def post(self, request, format=None):
        '''
        Endpoint to add user to a group
        '''
        data = request.data
        data['op'] = 'groupeditmembers'
        data['token'] = MESIBO_APPTOKEN
        data['cs'] = 1
        data['cr'] = 1
        data['delete'] = 0
        try:
            response = requests.post('https://api.mesibo.com/api.php', data=data)
            response = response.json()
            group = Group.objects.get(gid=data['gid'])
            emails = data['m'].split(',')
            group.uni_ids = [Mail(email=email) for email in emails]
            group.save()
            return Response({ 'message': 'success' }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({ 'message': 'failure' }, status=status.HTTP_400_BAD_REQUEST)
        
    
    def put(self, request, format=None):
        '''
        Endpoint to remove user from group
        '''
        data = request.data
        data['op'] = 'groupeditmembers'
        data['token'] = MESIBO_APPTOKEN
        data['cs'] = 1
        data['cr'] = 1
        data['delete'] = 1
        try:
            response = requests.post('https://api.mesibo.com/api.php', data=data)
            response = response.json()
            group = Group.objects.get(gid=data['gid'])
            emails_to_be_removed = data['m'].split(',')
            emails_all = [x.email for x in group.uni_ids]
            current_emails = set(emails_all) - set(emails_to_be_removed)
            current_emails = list(current_emails)
            group.uni_ids = [Mail(email=email) for email in current_emails]
            group.save()
            return Response({ 'message': 'success' }, status=status.HTTP_200_OK)
        except Exception as e:
            print('excpetion is ',e)
            return Response({ 'message': 'failure' }, status=status.HTTP_400_BAD_REQUEST)