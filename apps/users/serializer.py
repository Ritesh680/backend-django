from rest_framework import serializers
from rest_framework_simplejwt.tokens import AccessToken
from .models import User


class CustomAccessToken(AccessToken):
    """
    Custom access token class that works with our custom User model
    """

    @classmethod
    def for_user(cls, user):
        token = cls()
        token["user_id"] = user.id
        token["email"] = user.email
        return token


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "name", "email", "created_at", "updated_at"]


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["name", "email", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User.create_user(**validated_data)
        return user


class UserLoginSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(read_only=True)
    email = serializers.EmailField()
    access_token = serializers.CharField(read_only=True)
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        user = User.authenticate(attrs["email"], attrs["password"])
        if user is None:
            raise serializers.ValidationError("Invalid credentials")

        access_token = CustomAccessToken.for_user(user)

        response = {
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "access_token": str(access_token),
        }
        return response

    def create(self, validated_data):
        # For login, we don't create a new instance, just return the validated data
        # which contains the user information and access token from validate()
        return validated_data
