from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth import get_user_model

from .serializers import (RegistrationSerializer,
                          DateOfRegistrationSerializer
                          )

User = get_user_model()


class RigistrationView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)


class UserDateView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        serializer = DateOfRegistrationSerializer(request.user)
        return Response(serializer.data)

