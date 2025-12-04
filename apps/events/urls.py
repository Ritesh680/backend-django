from django.urls import path
from .views import EventListAPI

urlpatterns = [
    # This defines the endpoint /api/events/
    path("events/", EventListAPI.as_view(), name="event-list"),
]
