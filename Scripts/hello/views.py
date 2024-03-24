from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .models import UserProfile
from .serializers import UserProfileSerializer

# define view function - request handler
class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    
def home(request):
    return HttpResponse("Hello, Django!")