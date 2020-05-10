from rest_framework import  serializers

from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'email', 'linkedin_handle']

    def create(self, data):
        '''
        Create and return a new user instance
        '''
        return User.objects.create(**data)

    def update(self, instance, data):
        '''
        Update, save and return User instace
        '''
        instance.name = data.get('name', instance.name)
        instance.email = data.get('email', instance.email)
        instance.linkedin_handle = data.get('linkedin_handle', instance.linkedin_handle)
        instance.save()
        return instance

