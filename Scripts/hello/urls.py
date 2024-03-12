from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

class UserProfileViewSet(viewsets.ModelViewSet):
    ...
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

router = DefaultRouter()
router.register(r'users', views.UserProfileViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]