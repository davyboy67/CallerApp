from django.urls import path, include
from rest_framework import routers, viewsets
from rest_framework.routers import DefaultRouter
from . import views
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .views import create_profile, edit_profile, view_profile, delete_profile
class UserProfileViewSet(viewsets.ModelViewSet):
    ...
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

router = DefaultRouter()
router.register(r'users', views.UserProfileViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    # placeholder values for now until we have required items
    path('edit-profile/', edit_profile, name='edit_profile'),
    path('profile/', view_profile, name='profile'),
    path('create-profile/', create_profile, name='create_profile'),
    path('delete-profile/<int:id>', delete_profile, name='delete_profile')
]