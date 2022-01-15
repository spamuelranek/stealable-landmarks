
from rest_framework import permissions
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Landmark
from .serializer import LandmarkSerializer
from .permissions import IsPosterOrReadOnly, IsSignedinOrReadOnly


class LandmarkListView(ListCreateAPIView):
  permissions_classes = [permissions.IsAuthenticatedOrReadOnly]
  queryset = Landmark.objects.all()
  serializer_class = LandmarkSerializer

class LandmarkDetailView(RetrieveUpdateDestroyAPIView):
  queryset = Landmark.objects.all()
  serializer_class = LandmarkSerializer
  permission_classes = [IsPosterOrReadOnly]
