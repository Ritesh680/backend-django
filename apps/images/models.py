from django.db import models
import cloudinary


# Create your models here.

import re


class Image(models.Model):
    image = models.URLField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.image

    @staticmethod
    def upload_image(image_file):
        """Upload image to Cloudinary and return the Image instance"""
        response = cloudinary.uploader.upload(image_file)
        image_instance = Image(image=response["secure_url"])
        image_instance.save()
        return image_instance

    def delete_image(self):
        """
        Delete image from Cloudinary and database safely
        """
        try:
            print(f"Deleting Image ID: {self.id}")
            print(f"Cloudinary URL: {self.image}")

            if self.image:
                # Extract public_id from Cloudinary URL
                match = re.search(r"/upload/(?:v\d+/)?(.+)\.\w+$", self.image)
                if not match:
                    print("Failed to extract public_id from URL")
                else:
                    public_id = match.group(1)
                    print(f"Extracted public_id: {public_id}")
                    cloudinary.uploader.destroy(public_id)
                    print("Cloudinary deletion successful")
        except Exception as e:
            # Log error but continue to delete DB record
            print(f"Cloudinary deletion error: {e}")

        try:
            self.delete()
            print("Database record deleted successfully")
        except Exception as e:
            print(f"Database deletion error: {e}")
            raise e
