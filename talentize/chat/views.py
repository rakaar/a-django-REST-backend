from django.shortcuts import render
from django.core.mail import send_mail

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

import requests
import datetime
from logging import getLogger

from user.utils import MESIBO_APPTOKEN, MESIBO_APP_ID
from .models import Group, Mail, MsgRefer, MsgReferBy
from user.models import User

logger = getLogger(__name__)


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
            response = requests.post(
                'https://api.mesibo.com/api.php', data=data)
            gid = response.json()['group']['gid']
            name = data['name']
            group = Group(gid=gid, name=name)
            group.save()
            return Response({'message': 'success', 'gid': gid, 'name': name}, status=status.HTTP_200_OK)
        except Exception as e:
            logger.error('Error in MesiboGroup POST is ', e)
            return Response({'message': 'failure'}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, gid, format=None):
        '''
        To get users of a group
        '''
        try:
            group = Group.objects.get(gid=gid)
            users = [x.email for x in group.uni_ids]
            return Response({'users': users}, status=status.HTTP_200_OK)
        except Exception as e:
            logger.error('Error in MesiboGroup GET is ', e)
            return Response({'message': 'not found'}, status=status.HTTP_400_BAD_REQUEST)


class MesiboUser(APIView):
    '''
    Endpoints to handle user operations related to group
    '''

    def get(self, request, format=None):
        '''
        Endpoint toget groups of a user
        '''
        try:
            email = request.data['email']
            user = User.objects.get(email=email)
            groups = [(x.gid, x.status) for x in user.mesibo_details.groups]
            return Response({'groups': groups}, status=status.HTTP_200_OK)
        except Exception as e:
            logger.error('Error in MesiboUser GET is ', e)
            return Response({'message': 'not found'}, status=status.HTTP_400_BAD_REQUEST)

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
            response = requests.post(
                'https://api.mesibo.com/api.php', data=data)
            response = response.json()
            group = Group.objects.get(gid=data['gid'])
            emails = data['m'].split(',')
            group.uni_ids = [Mail(email=email) for email in emails]
            group.save()
            return Response({'message': 'success'}, status=status.HTTP_200_OK)
        except Exception as e:
            logger.error('Error in MesiboUser POST is ', e)
            return Response({'message': 'failure'}, status=status.HTTP_400_BAD_REQUEST)

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
            response = requests.post(
                'https://api.mesibo.com/api.php', data=data)
            response = response.json()
            group = Group.objects.get(gid=data['gid'])
            emails_to_be_removed = data['m'].split(',')
            emails_all = [x.email for x in group.uni_ids]
            current_emails = set(emails_all) - set(emails_to_be_removed)
            current_emails = list(current_emails)
            group.uni_ids = [Mail(email=email) for email in current_emails]
            group.save()
            return Response({'message': 'success'}, status=status.HTTP_200_OK)
        except Exception as e:
            logger.error('Error in MesiboUser PUT is ', e)
            return Response({'message': 'failure'}, status=status.HTTP_400_BAD_REQUEST)


class Complaint(APIView):
    '''
    Endpoint to email complaints from users to moderators
    '''

    def post(self, request, format=None):
        '''
        Endpoint to handle POST request 
            of user complaints in group chats
        '''

        data = request.data
        by_user_email = data['complaint_by']
        on_user_email = data['complaint_on']
        try:
            by_user_name = User.objects.get(email=by_user_email).name
            on_user_name = User.objects.get(email=on_user_email).name
        except Exception as e:
            logger.error('Error in Complaint POST is ', e)
            return Response({'message': 'invalid email'}, status=status.HTTP_400_BAD_REQUEST)
        gid = data['gid']
        try:
            group = Group.objects.get(gid=gid)
        except Exception as e:
            logger.error('Error in Complaint POST is ', e)
            return Response({'message': 'invalid group'}, status=status.HTTP_400_BAD_REQUEST)
        group_name = group.name
        now = datetime.datetime.now()
        plain_message = '{} [{}] was reported by {} [{}] in the group, {}, on {}'.format(
            on_user_name, on_user_email, by_user_name, by_user_email, group_name, now)
        try:
            send_mail(
                'User Complaint',
                plain_message,
                'llr.hall.complaints@gmail.com',
                ['pankaj08072000@gmail.com'],  # Moderator Email
            )
            return Response({'message': 'success'}, status=status.HTTP_200_OK)
        except Exception as e:
            logger.error('Error in Complaint POST is ', e)
            return Response({'message': 'failed to send mail'}, status=status.HTTP_400_BAD_REQUEST)


class ReferMsg(APIView):
    '''
    Endpoints to get all the message referals of a group
    '''

    def get(self, request, format=None):
        '''
        Endpoint to get refered messages in a group chat
        '''
        gid = request.data['gid']
        try:
            group = Group.objects.get(gid=gid)
            refer_msgs_data = []
            for refer in group.msg_refers:
                refer_dict = {}
                refer_dict[refer.refer_to] = [
                    x.refer_by for x in refer.refer_by]
                refer_msgs_data.append(refer_dict)
            return Response({'data': refer_msgs_data}, status=status.HTTP_200_OK)
        except Exception as e:
            logger.error('Error in ReferMsg GET is ', e)
            return Response({'message': 'invalid gid'}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, format=None):
        '''
        Endpoint to store message references to another
                in the group chat
        '''
        data = request.data
        gid = data['gid']
        refered_msg = data['refered_msg']
        refered_by = data['refered_by']
        # reference = MsgRefer(refer_to=refer_to, )
        try:
            group = Group.objects.get(gid=gid)
        except Exception as e:
            logger.error('Error in ReferMsg POST is ', e)
            return Response({'message': 'invalid gid'}, status=status.HTTP_400_BAD_REQUEST)

        if group.msg_refers is None:
            group.msg_refers = [MsgRefer(refer_to=refered_msg, refer_by=[
                                         MsgReferBy(refer_by=refered_by)])]
            group.save()
            return Response({'message': 'success'}, status=status.HTTP_200_OK)
        else:
            for ref_ind in range(len(group.msg_refers)):
                if group.msg_refers[ref_ind].refer_to == refered_msg:
                    group.msg_refers[ref_ind].refer_by.append(
                        MsgReferBy(refer_by=refered_by))
                    group.save()
                    return Response({'message': 'success'}, status=status.HTTP_200_OK)

            group.msg_refers.append(MsgRefer(refer_to=refered_msg, refer_by=[
                                    MsgReferBy(refer_by=refered_by)]))
            return Response({'message': 'success'}, status=status.HTTP_200_OK)
        return Response({'message': 'failure'}, status=status.HTTP_503_SERVICE_UNAVAILABLE)
