from django.db import models

# Create your models here.
from django.db import models


class UserProfile(models.Model):
    firebase_uid = models.CharField(max_length=128, unique=True, db_index=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    surname = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(max_length=255, unique=True)
    phone_number = models.CharField(max_length=20, unique=True, null=True, blank=True)
    is_service_provider = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # Preferences
    block_unknown_calls = models.BooleanField(default=False)
    voicemail_enabled = models.BooleanField(default=True)
    voicemail_greeting = models.TextField(null=True, blank=True)

    class Meta:
        app_label = "user_profile"


class ServiceProvider(models.Model):
    user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE, related_name='service_provider')
    company_name = models.CharField(max_length=255)
    service_type = models.CharField(max_length=255)
    verified = models.BooleanField(default=False)
    registration_number = models.CharField(max_length=255, null=True, blank=True)
    business_description = models.TextField(null=True, blank=True)
    website_url = models.URLField(max_length=255, null=True, blank=True)
    # Possible addition: Address, Operating Hours

    class Meta:
        app_label = "service_provider"

    # #TO-DO: All Tables should have a meta tag

class CallRecord(models.Model):
    caller = models.ForeignKey(UserProfile, related_name='made_calls', on_delete=models.CASCADE)
    receiver = models.ForeignKey(UserProfile, related_name='received_calls', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50)  # E.g., "Completed", "Missed", "Blocked", "Spam"
    authenticated = models.BooleanField(default=False)
    duration = models.IntegerField(help_text="Duration in seconds", null=True, blank=True)  # For completed calls

    class Meta:
        app_label = "call_record"

class UserFeedback(models.Model):
    call_record = models.ForeignKey(CallRecord, on_delete=models.CASCADE)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = "user_feedback"

class AnalyticsData(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    event_type = models.CharField(max_length=255)
    data = models.JSONField()
    timestamp = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        app_label = "analytics_data"