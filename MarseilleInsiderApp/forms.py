# forms.py
from django import forms
from .models import Client

class InscriptionForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['nom_client', 'prenom_client','tel_client','num_voie', 'name_voie', 'code_postal','ville','nom_utilisateur','mdp_utilisateur']
