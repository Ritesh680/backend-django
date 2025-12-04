from rest_framework import generics
from .models import Image
from .serializer import ImageCreateSerializer, ImageSerializer

# Create your views here.


class ImageListAPI(generics.ListAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer


class ImageDetailAPI(generics.RetrieveAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    lookup_field = "id"


class ImageCreateAPI(generics.CreateAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageCreateSerializer


class ImageUpdateAPI(generics.UpdateAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer


class ImageDeleteAPI(generics.DestroyAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
