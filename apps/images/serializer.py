from rest_framework import serializers

from apps.images.models import Image


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = "__all__"

    def create(self, validated_data):
        image = Image.upload_image(**validated_data)
        return image


class ImageCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ["image"]

    def create(self, validated_data):
        image = Image.upload_image(**validated_data)
        return image
