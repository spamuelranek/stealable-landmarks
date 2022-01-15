import imp
from django.forms import models
from rest_framework import serializers
from .models import Landmark

class LandmarkSerializer(serializers.ModelSerializer):
  class Meta:
    model = Landmark
    fields = ('title', 'poster', 'rating_of_stealablity', 'member_of_which_evil_organization', 'location')