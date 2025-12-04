from rest_framework import generics
from .models import Event
from .serializer import EventSerializer


# ListAPIView automatically handles GET requests and returns a list of items
class EventListAPI(generics.ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
