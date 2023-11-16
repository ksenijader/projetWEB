# myapp/backends.py
from django.contrib.auth.backends import ModelBackend
from .models import Client

class ClientAuthenticationBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            client = Client.objects.get(nom_utilisateur=username)
        except Client.DoesNotExist:
            return None
        if client.check_password(password):
            return client

