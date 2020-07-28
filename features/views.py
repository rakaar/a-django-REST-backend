from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

import  logging

from .models import LearnerList as LearnerListModel

logging.config.fileConfig('logs/config.ini')
logger = logging.getLogger(__name__)

class AllLearnLists(APIView):
	'''
	Endpoints to fetch all lists
	'''

	def get(self, request, format=None):
		'''
		GET endpoint to send all the displayed data of lists
		'''
		learn_lists = LearnerListModel.objects.all()
		learn_lists_arr = []
		for learn_list in learn_lists:
			learn_lists_arr.append({
				"id": learn_list.id,
				"person": {
					"name": learn_list.person_name,
					"fb": learn_list.person_fb,
					"linkedin": learn_list.person_linkedin,
					"numouno": learn_list.person_numouno,
					"pic": "https://api.numouno.tech/media/"+str(learn_list.person_pic)
				},
				"category": learn_list.category,
				"podcast": learn_list.podcast,
				"experiences": [exp.detail for exp in learn_list.experience],
				})
		return Response(learn_lists_arr, status=status.HTTP_200_OK)


class IndivLearnList(APIView):
	'''
	Fetch individual learnlist
	'''

	def get(self, request, id, format=None):
		'''
		GET endpoint to fetch complete details of a list by id
		'''
		try:
			learn_list = LearnerListModel.objects.filter(id=id).first()
		except Exception as e:
			logger.error('Error in fetching indivLearnList GET endpoint ', exc_info=1)
			return Response({"message": "wrong id"}, status=status.HTTP_400_BAD_REQUEST)

		resources = []
		for resource in learn_list.resources:
			resources.append({
				"title": resource.title,
				"link": resource.link,
				"level": resource.level,
				"tags": resource.tags,
				"description": resource.description,
				"cover": resource.cover
				}
			)
		learn_list_dict = {
			"id": learn_list.id,
			"person": {
				
				"name": learn_list.person_name,
				"fb": learn_list.person_fb,
				"linkedin": learn_list.person_linkedin,
				"numouno": learn_list.person_numouno,
				"pic": "https://api.numouno.tech/media/"+str(learn_list.person_pic)
			},
			"category": learn_list.category,
			"podcast": learn_list.podcast,
			"experiences": [exp.detail for exp in learn_list.experience],
			"resources": resources
		}
		return Response(learn_list_dict, status=status.HTTP_200_OK)
