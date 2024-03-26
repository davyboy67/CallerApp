from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from rest_framework import viewsets
from .models import UserProfile
from .forms import ProfileForm
from .serializers import UserProfileSerializer
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# define view function - request handler
class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    
def home(request):
    return HttpResponse("Hello, Django!")

def create_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_url')  
    else:
        form = ProfileForm()
    return render(request, 'create_profile.html', {'form': form})

def delete_profile(request, id):
    user = get_object_or_404(UserProfile, pk=id)
    if request.method == 'POST':
        user.delete()
        return redirect('success_url')  # Replace 'success_url' with the URL you want to redirect to after successful deletion
    return render(request, 'delete_profile.html', {'user': user})

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


