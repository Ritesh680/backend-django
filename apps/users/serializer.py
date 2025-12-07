from rest_framework import serializers
from rest_framework_simplejwt.tokens import AccessToken
from .models import User
from apps.images.models import Image


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
    avatar = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ["id", "name", "email", "avatar", "created_at", "updated_at"]

    def get_avatar(self, obj):
        """Get the avatar image URL from the Image model"""
        if obj.avatar:
            try:
                image = Image.objects.get(id=obj.avatar)
                return image.image
            except Image.DoesNotExist:
                return None
        return None


class UserCreateSerializer(serializers.ModelSerializer):
    avatar = serializers.IntegerField(required=False)

    class Meta:
        model = User
        fields = ["name", "email", "password", "avatar"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User.create_user(**validated_data)
        return user


class UserLoginSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(read_only=True)
    email = serializers.EmailField()
    avatar = serializers.URLField(read_only=True, allow_null=True)
    access_token = serializers.CharField(read_only=True)
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        user = User.authenticate(attrs["email"], attrs["password"])
        if user is None:
            raise serializers.ValidationError("Invalid credentials")

        access_token = CustomAccessToken.for_user(user)

        # Get avatar URL if avatar ID exists
        avatar_url = None
        if user.avatar:
            try:
                image = Image.objects.get(id=user.avatar)
                avatar_url = image.image
            except Image.DoesNotExist:
                pass

        response = {
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "avatar": avatar_url,
            "access_token": str(access_token),
        }
        return response

    def create(self, validated_data):
        # For login, we don't create a new instance, just return the validated data
        # which contains the user information and access token from validate()
        return validated_data
