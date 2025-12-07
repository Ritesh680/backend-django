from rest_framework import serializers

from apps.images.models import Image


class ImageSerializer(serializers.ModelSerializer):
    """Serializer for reading Image data"""

    class Meta:
        model = Image
        fields = "__all__"
        read_only_fields = ("created_at", "updated_at")


class ImageCreateSerializer(serializers.Serializer):
    """Serializer for creating Image with file upload"""

    image = serializers.ImageField(required=True)

    def create(self, validated_data):
        """Upload image to Cloudinary and save URL to database"""
        image_file = validated_data["image"]
        image_instance = Image.upload_image(image_file)
        return image_instance

    def to_representation(self, instance):
        """Return the created image data using ImageSerializer"""
        return ImageSerializer(instance).data


class ImageDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = []  # no fields required for deletion
