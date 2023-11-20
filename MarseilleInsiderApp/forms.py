# forms.py
from django import forms
from .models import Client
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth import password_validation

class InscriptionForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['nom_client', 'prenom_client','tel_client','num_voie', 'name_voie', 'code_postal','ville','nom_utilisateur','mdp_utilisateur','email']

class ClientUpdateForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['nom_client', 'prenom_client','tel_client','num_voie', 'name_voie', 'code_postal','ville']

class CustomPasswordResetForm(PasswordResetForm):
    username = forms.CharField(label="Username")
    nouveau_mdp = forms.CharField(
        label="Nouveau mot de passe",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
    )
    confirmer_mdp = forms.CharField(
        label="Confirmer le mot de passe",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
    )

    class Meta:
        model = Client
        fields = ['nom_utilisateur', 'nouveau_mdp', 'confirmer_mdp']

    def clean(self):
        cleaned_data = super().clean()
        nouveau_mdp = cleaned_data.get('nouveau_mdp')
        confirmer_mdp = cleaned_data.get('confirmer_mdp')

        if nouveau_mdp and confirmer_mdp and nouveau_mdp != confirmer_mdp:
            self.add_error('confirmer_mdp', "Les mots de passe ne correspondent pas.")

        # Use Django's built-in password validation
        try:
            password_validation.validate_password(nouveau_mdp)
        except forms.ValidationError as error:
            self.add_error('nouveau_mdp', error)

        return cleaned_data