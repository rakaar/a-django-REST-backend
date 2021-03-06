from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from user.utils import check_token
from user.models import User

# from .models import OnlineCourse, Patent, Project, PoR, ResearchPaper, PrevIntern, Position, Competition, Certification, Skill, Place, Preferences, College, CollegeCourse
from .models import Profile as ProfileModel

class Profile(APIView):
    '''
    Endpoint to get all profile details
    '''

    def post(self, request, format=None):
        '''
        handle request to POST profile
            verify user and returns user profile details
        '''
        # email = request.data['email']
        # if not check_token(email, request.data['token']):
        #     return Response({'message': 'invalid token'}, status=status.HTTP_400_BAD_REQUEST)

        # try:
        #     user = User.objects.get(email=email)
        # except User.DoesNotExist:
        #     return Response({'message': 'invalid user'}, status=status.HTTP_401_UNAUTHORIZED)
        # else:
        #     profile = user.profile
        #     name = user.name
            # return Response({'name': name}, status=status.HTTP_200_OK)
        return Response({'msg': 'temp down'}, status=status.HTTP_200_OK)



class Education(APIView):
    '''
    Endpoint to update education details in profile
    '''

    def post(self, request, format=None):
        '''
        handle POST request to update user profile
            college,school and online courses updated
        '''
        # email = request.data['email']
        # if not check_token(email, request.data['token']):
        #     return Response({'message': 'invalid token'}, status=status.HTTP_400_BAD_REQUEST)

        # try:
        #     user = User.objects.get(email=email)
        # except User.DoesNotExist:
        #     return Response({'message': 'invalid user'}, status=status.HTTP_401_UNAUTHORIZED)
        # else:
        #     user.profile.school = request.data['education']['school']
        #     user.profile.online_courses = [OnlineCourse(
        #         company=x['company'], name=x['name'], partner_insti=x['partner_insti']) for x in request.data['education']['online_courses']]
        #     user.profile.colleges = [College(
        #         name=x['name'], cgpa_range=x['cgpa_range'], dept=x['dept'], from_date=x[
        #             'from_date'], to_date=x['to_date'], type_of_degree=x['type_of_degree'],
        #         core_courses=[CollegeCourse(name=y['name'])
        #                       for y in x['core_courses']],
        #         additional_courses=[CollegeCourse(name=y['name']) for y in x['additional_courses']]) for x in request.data['education']['colleges']]

        #     user.save()
        return Response({'message': 'temp down'}, status=status.HTTP_200_OK)


class Experience(APIView):
    '''
    Endpoint to update experience details in profile
    '''

    def post(self, request, format=None):
        '''
        Handle POST request to update user profile
            Interns, Projects, POR, Research papers, Patents updated
        '''
        # email = request.data['email']
        # if not check_token(email, request.data['token']):
        #     return Response({'message': 'invalid token'}, status=status.HTTP_400_BAD_REQUEST)

        # try:
        #     user = User.objects.get(email=email)
        # except User.DoesNotExist:
        #     return Response({'message': 'invalid user'}, status=status.HTTP_401_UNAUTHORIZED)
        # else:
        #     user.profile.prev_interns = [PrevIntern(
        #         company=x['company'], job_title=x['job_title'], from_date=x['from_date'], to_date=x['to_date'], nature=x['nature']) for x in request.data['experience']['prev_interns']]
        #     user.profile.projects = [Project(
        #         project_type=x['project_type'], title=x['title'], description=x['description'], associated_info=x['associated_info']) for x in request.data['experience']['projects']]
        #     user.profile.por = [PoR(
        #         place=x['place'], positions=[Position(year=y['year'], description=y['description']) for y in x['positions']]) for x in request.data['experience']['por']]
        #     user.profile.research_papers = [ResearchPaper(
        #         journal=x['journal'], title=x['title'], description=x['description'], num_of_people=x['num_of_people'], is_main=x['is_main'], name_of_main=x['name_of_main']) for x in request.data['experience']['research_papers']]
        #     user.profile.patents = [Patent(
        #         date=x['date'], title=x['title'], description=x['description']) for x in request.data['experience']['patents']]
        #     user.save()
        return Response({'message': 'temp down'}, status=status.HTTP_200_OK)


class Achievement(APIView):
    '''
    Endpoint to update achievement details in profile
    '''

    def post(self, request, format=None):
        '''
        Handle POST request to update user profile
            Competitions, Certifications updated
        '''
        # email = request.data['email']
        # if not check_token(email, request.data['token']):
        #     return Response({'message': 'invalid token'}, status=status.HTTP_400_BAD_REQUEST)

        # try:
        #     user = User.objects.get(email=email)
        # except User.DoesNotExist:
        #     return Response({'message': 'invalid user'}, status=status.HTTP_401_UNAUTHORIZED)
        # else:
        #     user.profile.competitions = [Competition(
        #         title=x['title'], description=x['description'], date=x['date'], issuing_auth=x['issuing_auth']) for x in request.data['achs']['competitions']]
        #     user.profile.certifications = [Certification(
        #         name=x['name'], description=x['description'], year=x['year'], issuing_auth=x['issuing_auth']) for x in request.data['achs']['certifications']]
        #     user.save()
        return Response({'message': 'success'}, status=status.HTTP_200_OK)


class Personal(APIView):
    '''
    Endpoint to update Personal details in profile
    '''

    def post(self, request, format=None):
        '''
        Handle POST request to update user profile
            Location, Skills updated
        '''
        # email = request.data['email']
        # if not check_token(email, request.data['token']):
        #     return Response({'message': 'invalid token'}, status=status.HTTP_400_BAD_REQUEST)

        # try:
        #     user = User.objects.get(email=email)
        # except User.DoesNotExist:
        #     return Response({'message': 'invalid user'}, status=status.HTTP_401_UNAUTHORIZED)
        # else:
        #     user.profile.location = request.data['personal']['location']
        #     user.profile.skills = [Skill(name=x['name'])
        #                            for x in request.data['personal']['skills']]
        #     user.profile.bio = request.data['personal']['bio']
        #     pref_sectors_instance = [Place(
        #         name=x['name']) for x in request.data['personal']['preferences']['prefered_sectors']]
        #     pref_interns_instance = [Place(
        #         name=x['name']) for x in request.data['personal']['preferences']['prefered_interns']]
        #     pref_jobs_instance = [Place(
        #         name=x['name']) for x in request.data['personal']['preferences']['prefered_jobs']]
        #     user.profile.preferences = [Preferences(
        #         prefered_sectors=pref_sectors_instance, prefered_interns=pref_interns_instance, prefered_jobs=pref_jobs_instance)]
        #     user.save()
        return Response({'message': 'temp down'}, status=status.HTTP_200_OK)


class ProPic(APIView):
    '''
    Endpoints to handle profile pic upload
    '''

    def post(self, request, format=None):
        '''
        POST request to upload file to the server
        '''
        email = request.data['email']
        if not check_token(email, request.data['token']):
            return Response({'message': 'invalid token'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({'message': 'invalid user'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            user.profile.pro_pic = request.data['pro_pic']
            user.save()
        return Response({'message': 'success'}, status=status.HTTP_200_OK)

    
    def get(self, request, format=None):
        '''
        GET endpoint to fetch name
        '''
        email = request.data['email']
        if not check_token(email, request.data['token']):
            return Response({'message': 'invalid token'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({'message': 'invalid user'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            pro_pic = 'http://localhost:8000/media/' + str(user.profile.pro_pic)
        return Response({'pro_pic': pro_pic}, status=status.HTTP_200_OK)
            
