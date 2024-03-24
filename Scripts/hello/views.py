from django.shortcuts import render, redirect
from django.http import HttpResponse
from rest_framework import viewsets
from .models import UserProfile
from .forms import ProfileForm
from .serializers import UserProfileSerializer

# define view function - request handler
class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    
def home(request):
    return HttpResponse("Hello, Django!")

def edit_profile(request):
    profile = request.user.profile

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile)

    return render(request, 'edit_profile.html', {'form': form})

def view_profile(request):
    return render(request, 'view_profile.html')