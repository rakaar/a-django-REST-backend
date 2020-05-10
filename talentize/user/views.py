from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response


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
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

