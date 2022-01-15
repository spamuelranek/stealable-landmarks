from rest_framework import permissions
from django.contrib.auth import get_user_model

class IsPosterOrReadOnly(permissions.BasePermission):
  
  def has_object_permission(self, request, view, obj):
      if request.method == 'GET':
        return True
      
      return obj.poster == request.user

class IsSignedinOrReadOnly(permissions.IsAuthenticatedOrReadOnly):
  def has_permission(self, request, view):
      if request.method in permissions.SAFE_METHODS:
        return True

      if request.user in get_user_model():
        return True

      return False
      
