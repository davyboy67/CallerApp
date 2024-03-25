from django.apps import AppConfig
import firebase_admin
from firebase_admin import credentials

# cred = credentials.Certificate('path/to/serviceAccountKey.json')
# firebase_admin.initialize_app(cred)


class HelloConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'hello'
