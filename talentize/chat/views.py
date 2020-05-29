from django.shortcuts import render

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

import requests
from user.utils import MESIBO_APPTOKEN, MESIBO_APP_ID
# Create your views here.


class Group(APIView):
    '''
    Endpoint to manage groups
    '''
