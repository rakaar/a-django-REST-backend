from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from user.utils import check_token
from user.models import User

from .models import OnlineCourse, Patent, Project, PoR, ResearchPaper, PrevIntern, Position


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
        request.data.education : {
            'college': {
                'name': string,
                'cgpa_range': string,
                'dept': string,
                'core_courses': [],
                'additional_courses': []
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
            user.profile.online_courses = [OnlineCourse(
                company=x['company'], name=x['name'], partner_insti=x['partner_insti']) for x in request.data['education']['online_courses']]
            user.save()
            return Response({'message': 'success'}, status=status.HTTP_200_OK)


class Experience(APIView):
    '''
    POST endpoint to update experience details in profile

    {
                "prev_interns":[
                    {
                        "company":"VALVE",
                        "job_title":"Game Developer",
                        "from_date":"yesterday",
                        "to_date":"tomorrow",
                        "nature":"wfh"
                    }
                ],
                "projects":[
                    {
                        "project_type":"good type",
                        "title":"good project",
                        "description":"good desc",
                        "associated_info":"good AI"
                    }
                ],
                "por":[
                    {
                        "place":"home sweet home",
                        "positions":[
                            {
                                "year":"2018",
                                "description":"kid"
                            },
                            {
                                "year":"2020",
                                "description":"kid with corona"
                            }
                        ]

                    }
                ],
                "research_papers":[
                    {
                        "journal":"lul",
                        "title":"lol",
                        "description":"lel",
                        "num_of_people":25,
                        "is_main":1,
                        "name_of_main":"Pankaj"

                    }
                ],
                "patents":[
                    {
                        "title":"GG",
                        "description":"WP",
                        "date":"today"
                    }
                ]

    }

    '''

    def post(self, request, format=None):
        '''
        Handle post request to /profile/experience
        '''
        email = request.data['email']
        if not check_token(email, request.data['token']):
            return Response({'message': 'invalid token'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({'message': 'invalid user'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            user.profile.prev_interns = [PrevIntern(
                company=x['company'], job_title=x['job_title'], from_date=x['from_date'], to_date=x['to_date'], nature=x['nature']) for x in request.data['experience']['prev_interns']]
            user.profile.projects = [Project(
                project_type=x['project_type'], title=x['title'], description=x['description'], associated_info=x['associated_info']) for x in request.data['experience']['projects']]
            user.profile.por = [PoR(
                place=x['place'], positions=[Position(year=y['year'], description=y['description']) for y in x['positions']]) for x in request.data['experience']['por']]
            user.profile.research_papers = [ResearchPaper(
                journal=x['journal'], title=x['title'], description=x['description'], num_of_people=x['num_of_people'], is_main=x['is_main'], name_of_main=x['name_of_main']) for x in request.data['experience']['research_papers']]
            user.profile.patents = [Patent(
                date=x['date'], title=x['title'], description=x['description']) for x in request.data['experience']['patents']]
            user.save()
            return Response({'message': 'success'}, status=status.HTTP_200_OK)
