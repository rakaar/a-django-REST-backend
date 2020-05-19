from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from user.utils import check_token
from user.models import User

from .models import OnlineCourse, Competition, Certification, Skill

class Profile(APIView):
    '''
    GET endpoint to get all profile details
    '''

    def get(self, request, format=None):
        email = request.data['email']
        if not check_token(email, request.data['token']):
            return Response({'message': 'invalid token'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            user = User.objects.filter(email=email)[0]
        except User.DoesNotExist:
            return Response({'message': 'invalid user'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            profile = user.profile
            return Response(profile, status=status.HTTP_200_OK)

class Education(APIView):
    '''
    POST endpoint to update education details in profile
    '''

    def post(self, request, format=None):
        '''
        request.data['education'] : {
            'college': {
                'name': string,
                'cgpa_range': string,
                'dept': string,
                'core_courses': [{'name' : string}],
                'additional_courses': [{'name' : string}]
            },
            'school': {
                'name': string,
                'board': string,
                percentage: string
            },
            'online_courses': [
                { 'name' : string, 'company': string, 'partner_insti': string }
            ]
        }
        ''' 
        email = request.data['email']
        if not check_token(email, request.data['token']):
            return Response({'message': 'invalid token'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({'message': 'invalid user'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            user.profile.college = request.data['education']['college']
            user.profile.school = request.data['education']['school']
            user.profile.online_courses = [OnlineCourse(company=x['company'], name=x['name'], partner_insti=x['partner_insti']) for x in request.data['education']['online_courses']]
            user.save()
            return Response({ 'message': 'success'}, status=status.HTTP_200_OK)


class Achievement(APIView):
    '''
    POST endpoint to update achievement details in profile
    '''

    def post(self, request, format=None):
        '''
        request.data['achs'] = {
            'competitions' : [
                { 'title' : string, 'description': string, 'date': string }
            ],
            'certifications': [
                { 'name': string, 'description' string, 'year': string }
            ]
        }
        '''
        email = request.data['email']
        if not check_token(email, request.data['token']):
            return Response({'message': 'invalid token'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({'message': 'invalid user'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            user.profile.competitions = [Competition(title=x['title'], description=x['description'], date=x['date']) for x in request.data['achs']['competitions']]
            user.profile.certifications = [Certification(name=x['name'], description=x['description'], year=x['year']) for x in request.data['achs']['certifications']]
            user.save()
            return Response({ 'message': 'success'}, status=status.HTTP_200_OK)


class Personal(APIView):
    '''
    POST endpoint to update Personal details in Profile
    '''

    def post(self, request, format=None):
        '''
        request.data['personal'] = {
            'skills' : [
                { 'name' string }
            ],
            'location: string
        }
        '''
        email = request.data['email']
        if not check_token(email, request.data['token']):
            return Response({'message': 'invalid token'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({'message': 'invalid user'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            user.profile.location = request.data['personal']['location']
            user.profile.skills = [Skill(name=x['name']) for x in request.data['personal']['skills']]
            user.save()
            return Response({ 'message': 'success'}, status=status.HTTP_200_OK)
