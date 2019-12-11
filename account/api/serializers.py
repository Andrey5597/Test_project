from rest_framework import serializers
from account.models import UserModel


class RegistrationSerializer(serializers.ModelSerializer):

    password2 = serializers.CharField(write_only=True)

    def save(self):

        user = UserModel(
            username=self.validated_data['username'],
            email=self.validated_data['email']
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password : Password must match'})
        user.set_password(password)
        user.save()

        return user

    class Meta:
        model = UserModel
        fields = ("username", "email", "password", "password2")


class DateOfRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['date_joined']
