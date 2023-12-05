from django.core.exceptions import ValidationError
from django.db import models
from django.shortcuts import render
from django.urls import reverse


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
        ('ETE', 'en Été'),
        ('HIVER', 'en Hiver'),
        ('AUTOMNE', 'en Automne'),
        ('PRINTEMPS', 'au Printemps'),
        ('TA',"toute l'Année")
    ]

    id_loisir = models.AutoField(primary_key=True)
    nom_loisir = models.CharField(max_length=255, verbose_name="Nom du loisir")
    num_voie = models.IntegerField(verbose_name="Numéro de la voie")
    nom_voie = models.CharField(max_length=50, verbose_name="Nom de la voie")
    code_postal = models.IntegerField(verbose_name="Code postale")
    ville = models.CharField(max_length=50, verbose_name="Ville")
    categorie = models.ForeignKey(Catégorie, on_delete=models.CASCADE)
    id_fournisseur = models.ForeignKey(Fournisseur, on_delete=models.CASCADE)
    prix_fournisseur = models.ForeignKey(Prix, on_delete=models.CASCADE)
    saisons = models.CharField(max_length=10, choices=SAISON_CHOICES, verbose_name="Saison")
    description=models.TextField(verbose_name="Description du loisir")

    def calcul_prix_total(self, nombre_personnes):
        if isinstance(nombre_personnes, int):
            prix_total = self.prix_fournisseur.prix_fournisseur * nombre_personnes
            return prix_total
        else:
            return None

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
            raise ValidationError("Le mot de passe doit contenir au moins 1 chiffre")
         if not any(not char.isalnum() for char in mdp):
            raise ValidationError("Le mot de passe doit contenir un caractère spécial")


class Client(models.Model):
    id_client = models.AutoField(primary_key=True)
    num_voie = models.IntegerField(verbose_name="Numéro de la voie")
    name_voie = models.CharField(max_length=50, verbose_name="Nom de la voie")
    code_postal = models.IntegerField(verbose_name="Code postale")
    ville = models.CharField(max_length=50, verbose_name="Ville")
    prenom_client = models.CharField(max_length=10, verbose_name="Prénom du client")
    nom_client = models.CharField(max_length=10, verbose_name="Nom du client")
    email=models.CharField(max_length=100,verbose_name="Email")
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
    is_authenticated=True

    def check_password(self, mdp):
        if self.mdp_utilisateur == mdp:
            return self
    def set_password(self,nouveau_mdp):
        self.mdp_utilisateur=nouveau_mdp

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    last_login = models.DateTimeField(auto_now=True)

    def get_reviews(self):
        return self.reviews.all()

class Pack(models.Model):
    id_pack = models.AutoField(primary_key=True)
    nom_pack = models.CharField(max_length=255, verbose_name="Nom du pack")
    nombre_loisirs = models.IntegerField(validators=[validate_nombre_format], verbose_name="Nombre")
    description = models.TextField(verbose_name="Description du loisir")
    prix_pack= models.IntegerField(verbose_name="Prix du pack")

    def prix_du_pack(self):

        loisirs_du_pack = self.contient_set.select_related('id_loisir__prix_fournisseur').all()
        prix_reduit = sum(loisir.id_loisir.prix_fournisseur.prix_fournisseur * 0.9 for loisir in loisirs_du_pack)

        return prix_reduit

    def loisirs_du_pack(self):
        loisirs_du_pack = self.contient_set.values_list('id_loisir__nom_loisir', flat=True)

        ids_loisirs = [id_loisir for id_loisir in loisirs_du_pack]
        return ', '.join(ids_loisirs)

    def get_ids_activites_du_pack(self):
        return list(self.contient_set.values_list('id_loisir', flat=True))

    def get_ids_and_noms_activites_du_pack(self):
        ids_activites = self.get_ids_activites_du_pack()
        id_nom_tuples = []

        for id_loisir in ids_activites:
            try:
                loisir = Loisir.objects.get(id_loisir=id_loisir)
                id_nom_tuples.append((id_loisir, loisir.nom_loisir))
            except Loisir.DoesNotExist:
                id_nom_tuples.append((id_loisir, f"Loisir #{id_loisir} non trouvé"))

        return id_nom_tuples



    def calcul_prix_total(self, nombre_personnes):
        prix_du_pack=self.prix_du_pack()
        if isinstance(nombre_personnes, int):
            prix_total = prix_du_pack * nombre_personnes
            return prix_total
        else:
            return None

class AchetePack(models.Model):
    date_achat_pack = models.DateField(verbose_name="Date d'achat du pack",auto_now_add=True)
    id_pack = models.ForeignKey(Pack, on_delete=models.CASCADE)
    id_client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='achetepack_id')



class AcheteLoisir(models.Model):  # Renamed to follow Python conventions
    date_achat_loisir = models.DateField(verbose_name="Date d'achat du loisir",auto_now_add=True)
    id_loisir = models.ForeignKey(Loisir, on_delete=models.CASCADE)
    id_client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='acheteloisirs_id')


class Contient(models.Model):
    id_loisir=models.ForeignKey(Loisir, on_delete=models.CASCADE)
    id_pack=models.ForeignKey(Pack, on_delete=models.CASCADE)

