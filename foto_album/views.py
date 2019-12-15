from django_filters import rest_framework as filters
from rest_framework import status
from rest_framework.filters import OrderingFilter
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from foto_album.filters import AlbumFilter, PictureFilter
from foto_album.models import Album, Picture

from foto_album.permissions import AlbumOwnerPermission, PictureOwnerPermission
from .serializers import (AlbumCreateSerializer, AlbumDetailSerializer, PictureUpdateSerializer,
                          PictureCreateBase64Serializer, AlbumUpdateSerializer,
                          PictureCreateSerializer, PictereDetailSerializer)


class AlbumCreateView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        serializer = AlbumCreateSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)


class UserAlbumsView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = AlbumDetailSerializer
    filter_backends = (filters.DjangoFilterBackend, OrderingFilter)
    filterset_class = AlbumFilter
    ordering_fields = ('id', 'title')

    def get_queryset(self):
        return Album.objects.filter(owner=self.request.user)


class PictureCreateView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        serializer = PictureCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)


class PictureCreateBase64View(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        serializer = PictureCreateBase64Serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)


class PicturesView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = PictereDetailSerializer
    filter_backends = (filters.DjangoFilterBackend, OrderingFilter)
    filterset_class = PictureFilter
    ordering_fields = ('id', 'title')

    def get_queryset(self):
        return Picture.objects.filter(album__owner=self.request.user)


class AlbumDetailsView(APIView):
    permission_classes = (IsAuthenticated, AlbumOwnerPermission)

    def get(self, request, album_id):
        album = self.album
        output_serializer = AlbumDetailSerializer(album)
        return Response(output_serializer.data)

    def put(self, request, album_id):
        album = self.album
        input_serializer = AlbumUpdateSerializer(album, data=request.data)
        input_serializer.is_valid(raise_exception=True)
        album = input_serializer.save()
        output_serializer = AlbumDetailSerializer(album)
        return Response(output_serializer.data)

    def delete(self, request, album_id):
        album = self.album
        album.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PictureDetailsView(APIView):
    permission_classes = (IsAuthenticated, PictureOwnerPermission)

    def get(self, request, picture_id):
        picture = self.picture
        output_serializer = PictereDetailSerializer(picture)
        return Response(output_serializer.data)

    def put(self, request, picture_id):
        picture = self.picture
        input_serializer = PictureUpdateSerializer(picture, data=request.data)
        input_serializer.is_valid(raise_exception=True)
        picture = input_serializer.save()
        output_serializer = PictereDetailSerializer(picture)
        return Response(output_serializer.data)

    def delete(self, request, picture_id):
        picture = self.picture
        picture.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


