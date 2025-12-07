from django.urls.conf import path
from apps.images.views import (
    ImageCreateApi,
    ImageDeleteApi,
    ImageDetailApi,
    ImageListApi,
)


urlpatterns = [
    path("images/", ImageListApi.as_view(), name="image-list"),
    path("images/create/", ImageCreateApi.as_view(), name="image-create"),
    path("images/<int:pk>/", ImageDetailApi.as_view(), name="image-detail"),
    path("images/<int:pk>/delete/", ImageDeleteApi.as_view(), name="image-delete"),
]
