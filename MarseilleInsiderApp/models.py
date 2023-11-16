from django.core.exceptions import ValidationError
from django.db import models


class Prix(models.Model):
    id_prix = models.AutoField(primary_key=True)
    prix_fournisseur = models.IntegerField(verbose_name="Prix fournisseur")



class Catégorie(models.Model):
    CATEGORIES_CHOICES = [
        ('GA', 'Gastronomie'),
        ('AC', 'Arts et culture'),
        ('NA', 'Nature et plein air'),
        ('BD', 'Bien être et détente'),
        ('ACR', "Ateliers créatifs"),
        ('EC', "En couple"),
        ('EF', "En famille"),
    ]
    categorie = models.CharField(max_length=50, choices=CATEGORIES_CHOICES, primary_key=True)



class Fournisseur(models.Model):
    EXCLUSIVITY_CHOICES = [
        ('OUI', 'Oui'),
        ('NON', 'Non'),
    ]

    id_fournisseur = models.AutoField(primary_key=True)
    nom_fournisseur = models.CharField(max_length=50, verbose_name="Nom du fournisseur")
    exclusivite = models.CharField(max_length=7, choices=EXCLUSIVITY_CHOICES, verbose_name="Titre exclusif")


class Loisir(models.Model):
    SAISON_CHOICES = [
        ('ETE', 'Été'),
        ('HIVER', 'Hiver'),
        ('AUTOMNE', 'Automne'),
        ('PRINTEMPS', 'Printemps'),
        ('TA','Toutes saisons')
    ]

    id_loisir = models.AutoField(primary_key=True)
    nom_loisir = models.CharField(max_length=255, verbose_name="Nom du loisir")
    num_voie = models.IntegerField(verbose_name="Numéro de la voie")
    name_voie = models.CharField(max_length=50, verbose_name="Nom de la voie")
    code_postal = models.IntegerField(verbose_name="Code postale")
    ville = models.CharField(max_length=50, verbose_name="Ville")
    categorie = models.ForeignKey(Catégorie, on_delete=models.CASCADE)
    id_fournisseur = models.ForeignKey(Fournisseur, on_delete=models.CASCADE)
    prix_fournisseur = models.ForeignKey(Prix, on_delete=models.CASCADE)
    saisons = models.CharField(max_length=10, choices=SAISON_CHOICES, verbose_name="Saison")
    description=models.TextField(verbose_name="Description du loisir")



# Validation functions

def validate_tel_format(numero):
    # Split the address into components
    components = [component.strip() for component in numero.split('.')]

    # Check if there are exactly four components
    if len(components) != 5:
        raise ValidationError("Numero must contain exactly 5 components")


def validate_nombre_format(nombre):
    if nombre is not None and nombre < 2:
        raise ValidationError("The number of hobbies in a pack must be greater than or equal to 2.")

def validate_mdp(mdp):
         if not any(char.isupper() for char in mdp):
             raise ValidationError("Le mot de passe doit contenir une majuscule")
         if not any(char.isdigit() for char in mdp):
            raise ValidationError("Le mot de apsse doit contenir au moins 1 chiffre")
         if not any(not char.isalnum() for char in mdp):
            raise ValidationError("Le mot de passe doit contenir un caract spé")



class Client(models.Model):
    id_client = models.AutoField(primary_key=True)
    num_voie = models.IntegerField(verbose_name="Numéro de la voie")
    name_voie = models.CharField(max_length=50, verbose_name="Nom de la voie")
    code_postal = models.IntegerField(verbose_name="Code postale")
    ville = models.CharField(max_length=50, verbose_name="Ville")
    prenom_client = models.CharField(max_length=10, verbose_name="Prénom du client")
    nom_client = models.CharField(max_length=10, verbose_name="Nom du client")
    tel_client = models.CharField(
        max_length=20,
        verbose_name="Numéro de téléphone du client",
        validators=[validate_tel_format],
        help_text="Le numéro doit être sous le format suivant: XX.XX.XX.XX.XX"
    )
    nom_utilisateur=models.CharField(max_length=20,
                                     verbose_name="Nom d'utilisateur",
                                     unique=True
                                    )
    mdp_utilisateur = models.CharField(max_length=20,
                                       verbose_name="Mot de passe utilisateur",
                                       validators=[validate_mdp],
                                       unique=True,
                                       help_text="Le mot de passe doit contenir au moins 1 majuscule, 1 chiffre et 1 caratère spécial"
                                       )


class Pack(models.Model):
    id_pack = models.AutoField(primary_key=True)
    nom_pack = models.CharField(max_length=10, verbose_name="Nom du pack")
    nombre_loisirs = models.IntegerField(validators=[validate_nombre_format], verbose_name="Nombre")
    description = models.TextField(verbose_name="Description du loisir")


class AchetePack(models.Model):
    date_achat_pack = models.DateField(verbose_name="Date d'achat du pack")
    id_pack = models.ForeignKey(Pack, on_delete=models.CASCADE)
    prix_client = models.ForeignKey(Prix, on_delete=models.CASCADE)



class AcheteLoisir(models.Model):  # Renamed to follow Python conventions
    date_achat_loisir = models.DateField(verbose_name="Date d'achat du loisir")
    id_loisir = models.ForeignKey(Loisir, on_delete=models.CASCADE)
    prix_client = models.ForeignKey(Client, on_delete=models.CASCADE)

class Contient(models.Model):
    id_loisir=models.ForeignKey(Loisir, on_delete=models.CASCADE)
    id_pack=models.ForeignKey(Pack, on_delete=models.CASCADE)