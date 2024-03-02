from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework.exceptions import AuthenticationFailed
from users.models import User


class UserRegisterSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(max_length=16, min_length=8, write_only=True)
    password2 = serializers.CharField(max_length=16, min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ("email", "first_name", "last_name", "password1", "password2")

    def validate(self, attrs):
        password1 = attrs.get('password1', '')
        password2 = attrs.get('password2', '')

        if password1 != password2:
            raise serializers.ValidationError("Parollar bir xil emas")
        return attrs

    def create(self, validate_data):
        user = User.objects.create_user(
            email=validate_data['email'],
            first_name=validate_data.get('first_name'),
            last_name=validate_data.get('last_name'),
            password=validate_data.get('password')
        )
        return user


class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=128)
    password = serializers.CharField(max_length=128)

    class Meta:
        model = User
        fields = ("username", "password")

    def validate(self, attrs):
        username = attrs.get("username")
        password = attrs.get("password")

        request = self.context.get("request")

        user = authenticate(request, username=username, password=password)
        if not user:
            raise AuthenticationFailed("Xatolik bor")

        return super().validate(attrs)
