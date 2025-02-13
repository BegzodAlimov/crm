from django.contrib.auth import authenticate
from django.contrib.auth.models import update_last_login
import random
import uuid
from tools.utility import validate_text
from users.models import  User
from rest_framework import serializers
from rest_framework.exceptions import ValidationError, NotFound
from rest_framework.generics import get_object_or_404
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenRefreshSerializer
from rest_framework_simplejwt.tokens import AccessToken


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'phone_number', 'gender', 'avatar', 'document', 'status')
        extra_kwargs = {
            'first_name': {'required': True, 'validators': [validate_text]},
            'last_name': {'required': True, 'validators': [validate_text]},
            'phone_number': {'required': False, 'validators': [validate_text]},
            'gender': {'required': False},
        }

    @staticmethod
    def get_username(first_name):
        temp_username = f'{first_name}-{uuid.uuid4().__str__().split("-")[-1]}' # instagram-23324fsdf
        while User.objects.filter(username=temp_username):
            temp_username = f"{temp_username}{random.randint(0,9)}"
        return temp_username

    def validate(self, data):
        new_username = self.get_username(data.get('first_name'))
        new_password = f'{(data.get("first_name").lower())}-{data.get("last_name").lower()}'
        data['username'] = new_username
        data['password'] = new_password

        print(data)

        return data

    def create(self, validated_data):
        user = User(**validated_data)
        user.save()
        return user

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'username', 'email','phone_number', 'status']


class SingleUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username', 'first_name', 'last_name', 'gender', 'email', 'avatar', 'document', 'status', 'password']
        extra_kwargs = {
            'id': {'read_only': True},
            'first_name': {'required': True, 'validators': [validate_text]},
            'last_name': {'required': True, 'validators': [validate_text]},
            'phone_number': {'required': False, 'validators': [validate_text]},
            'gender': {'required': False},
            "password": {"write_only": True},
        }

    def update(self, instance, validated_data):
        password = validated_data.get('password')
        if password:
            instance.set_password(password)
            validated_data.pop('password', None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance


class LoginSerializer(TokenObtainPairSerializer):
    def __init__(self, *args, **kwargs):
        super(LoginSerializer, self).__init__(*args, **kwargs)
        self.fields['username'] = serializers.CharField(write_only=True, required=True, validators=[validate_text])
        self.fields['password'] = serializers.CharField(write_only=True, required=True, validators=[validate_text])

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')
        current_user = User.objects.filter(username=username).first()

        if not current_user:
            raise ValidationError({'success': False, 'message': 'User not found'})

        user = authenticate(username=username, password=password)

        if not user:
            raise ValidationError({'success': False, 'message': 'Invalid credentials'})
        self.user = user
        token = self.user.token()
        user_serializer = SingleUserSerializer(self.user)
        return {'success': True, 'token': token,'user': user_serializer.data}


class AccessTokenRefreshSerializer(TokenRefreshSerializer):
    def validate(self, data):
        data = super().validate(data)
        access_token = data.get('access')
        if not access_token:
            raise serializers.ValidationError({"access_token": "This field is required."})

        try:
            access_token_instance = AccessToken(access_token)
            user_id = access_token_instance['user_id']
        except Exception:
            raise serializers.ValidationError({"access_token": "Invalid access token."})

        user = get_object_or_404(User, id=user_id)

        update_last_login(None, user)

        return data


class LogoutSerializer(serializers.Serializer):
    refresh_token = serializers.CharField()
