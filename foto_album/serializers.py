from rest_framework import serializers
from foto_album.models import Album, Picture
from drf_extra_fields.fields import Base64ImageField

from django.contrib.auth import get_user_model

User = get_user_model()


class AlbumCreateSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=50)
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

    def create(self, validated_data):
        return Album.objects.create(**validated_data)


class AlbumDetailSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=50)


class AlbumUpdateSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=50)

    def update(self, instance, validated_data):
        instance.title = validated_data['title']
        instance.save(update_fields=['title'])
        return instance


class PictureUpdateSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=50)

    def update(self, instance, validated_data):
        instance.title = validated_data['title']
        instance.save(update_fields=['title'])
        return instance


class PictureCreateSerializer(serializers.Serializer):
    image = serializers.ImageField()
    title = serializers.CharField(max_length=50)
    album = serializers.PrimaryKeyRelatedField(queryset=Album.objects.all())

    def create(self, validated_data):
        return Picture.objects.create(**validated_data)


class PictureCreateBase64Serializer(PictureCreateSerializer):
    image = Base64ImageField()


class PictereDetailSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    image = serializers.ImageField()
    title = serializers.CharField(max_length=50)
    album = AlbumDetailSerializer()
