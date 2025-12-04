import cloudinary
from django.db import models


# Create your models here.
class Image(models.Model):
    image = models.ImageField(upload_to="images/")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.image.name

    @staticmethod
    def upload_image(image):
        return cloudinary.uploader.upload(image)

    @staticmethod
    def delete_image(image):
        return cloudinary.uploader.destroy(image)
