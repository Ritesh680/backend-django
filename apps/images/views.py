# Create your views here.


from rest_framework import generics, status
from rest_framework.views import Response
from apps.images.models import Image
from apps.images.serializer import (
    ImageDeleteSerializer,
    ImageSerializer,
    ImageCreateSerializer,
)


class ImageListApi(generics.ListAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer


class ImageCreateApi(generics.CreateAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageCreateSerializer


class ImageDetailApi(generics.RetrieveAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    lookup_field = "pk"


class ImageDeleteApi(generics.GenericAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageDeleteSerializer
    lookup_field = "pk"

    def delete(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            instance.delete_image()
            return Response(
                {"message": "Image deleted successfully"},
                status=status.HTTP_204_NO_CONTENT,
            )
        except Image.DoesNotExist:
            return Response(
                {"error": "Image not found"}, status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            print(f"Server error: {e}")
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
