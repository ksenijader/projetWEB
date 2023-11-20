# myapp/backends.py
from django.contrib.auth.backends import ModelBackend
from .models import Client

class ClientAuthenticationBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            client = Client.objects.get(nom_utilisateur=username)
        except Client.DoesNotExist:
            return None
        if client.check_password(password) and self.user_can_authenticate(client):
            client.is_authenticated = True
            print(f"User {client} authenticated successfully.")
            return client
        else:
            print(f"Failed authentication attempt for user {username}.")

        return None

    def get_user(self, user_id):
        try:
            return Client.objects.get(id_client=user_id)
        except Client.DoesNotExist:
            return None

