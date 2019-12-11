from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import get_user_model

from .serializers import (RegistrationSerializer,
                          DateOfRegistrationSerializer
                          )
from rest_framework.authtoken.models import Token

User = get_user_model()


@api_view(['POST'])
def registration_view(request):

    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            user = serializer.save()
            data['response'] = 'Successfully created a new user'
            data['email'] = user.email
            data['username'] = user.username
            token = Token.objects.get(user=user).key
            data['token'] = token

            return Response(data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def date_of_user_registration_view(request):

    if request.method == 'GET':
        serializer = DateOfRegistrationSerializer(data=request.data)
        username = request.data['username']
        data = {}
        if serializer.is_valid():
            user = User.objects.get(username=username)
            data['date_joined'] = user.date_joined
            return Response(data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
