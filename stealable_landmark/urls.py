from django.urls import path
from .views import LandmarkDetailView, LandmarkListView


urlpatterns = [
  path("",LandmarkListView.as_view(), name = "landmark_list"),
  path("<int:pk>/",LandmarkDetailView.as_view(), name = "landmark_detail"),
]