from rest_framework import serializers
from django.contrib.auth import get_user_model
import uuid

User = get_user_model()


class RegistrationSerializer(serializers.Serializer):
    email = serializers.EmailField()
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    password = serializers.CharField()
    password2 = serializers.CharField()

    def validate_email(self, value):
        value = value.lower()
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError('User with this email already exists.')
        return value

    def validate_passwords(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError('Passwords don\'t match')
        return attrs

    def create(self, validated_data):
        del validated_data['password2']
        validated_data['username'] = uuid.uuid4().hex[:30]
        return User.objects.create_user(
            **validated_data
        )


class DateOfRegistrationSerializer(serializers.Serializer):
    date_joined = serializers.DateTimeField()
