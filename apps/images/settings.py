# Cloudinary configuration
import cloudinary

from club_config.settings.env import env

cloudinary.config(
    cloud_name=env("CLOUDINARY_CLOUD_NAME"),
    api_key=env("CLOUDINARY_API_KEY"),
    api_secret=env("CLOUDINARY_API_SECRET"),
)
