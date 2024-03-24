from django import forms
from .models import UserProfile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['name','surname', 'email', 'phone_number','block_unknown_calls', 'voicemail_enabled', 'voicemail_greeting']
