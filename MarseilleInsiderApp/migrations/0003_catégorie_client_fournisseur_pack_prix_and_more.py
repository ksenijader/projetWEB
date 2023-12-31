# Generated by Django 4.1 on 2023-11-15 20:00

import MarseilleInsiderApp.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MarseilleInsiderApp', '0002_rename_adresse_loisir_adresse_1'),
    ]

    operations = [
        migrations.CreateModel(
            name='Catégorie',
            fields=[
                ('categorie', models.CharField(choices=[('GA', 'Gastronomie'), ('AC', 'Arts et culture'), ('NA', 'Nature et plein air'), ('BD', 'Bien être et détente'), ('AC', 'Ateliers créatifs'), ('EC', 'En couple'), ('EF', 'En famille')], max_length=50, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id_client', models.AutoField(primary_key=True, serialize=False)),
                ('num_voie', models.IntegerField(verbose_name='Numéro de la voie')),
                ('name_voie', models.CharField(max_length=50, verbose_name='Nom de la voie')),
                ('code_postal', models.IntegerField(verbose_name='Code postale')),
                ('ville', models.CharField(max_length=50, verbose_name='Ville')),
                ('prenom_client', models.CharField(max_length=10, verbose_name='Prénom du client')),
                ('nom_client', models.CharField(max_length=10, verbose_name='Nom du client')),
                ('tel_client', models.CharField(help_text='Le numéro doit être sous le format suivant: XX.XX.XX.XX.XX', max_length=20, validators=[MarseilleInsiderApp.models.validate_tel_format], verbose_name='Numéro de téléphone du client')),
                ('nom_utilisateur', models.CharField(max_length=20, unique=True, verbose_name="Nom d'utilisateur")),
                ('mdp_utilisateur', models.CharField(help_text='Le mot de passe doit contenir au moins 1 majuscule, 1 chiffre et 1 caratère spécial', max_length=20, validators=[MarseilleInsiderApp.models.validate_mdp], verbose_name='Mot de passe utilisateur')),
            ],
        ),
        migrations.CreateModel(
            name='Fournisseur',
            fields=[
                ('id_fournisseur', models.AutoField(primary_key=True, serialize=False)),
                ('nom_fournisseur', models.CharField(max_length=50, verbose_name='Nom du fournisseur')),
                ('exclusivite', models.CharField(choices=[('OUI', 'Oui'), ('NON', 'Non')], max_length=7, verbose_name='Titre exclusif')),
            ],
        ),
        migrations.CreateModel(
            name='Pack',
            fields=[
                ('id_pack', models.AutoField(primary_key=True, serialize=False)),
                ('nom_pack', models.CharField(max_length=10, verbose_name='Nom du pack')),
                ('nombre_loisirs', models.IntegerField(validators=[MarseilleInsiderApp.models.validate_nombre_format])),
                ('description', models.TextField(verbose_name='Description du loisir')),
            ],
        ),
        migrations.CreateModel(
            name='Prix',
            fields=[
                ('id_prix', models.AutoField(primary_key=True, serialize=False)),
                ('prix_fournisseur', models.IntegerField(verbose_name='Prix fournisseur')),
            ],
        ),
        migrations.RenameField(
            model_name='loisir',
            old_name='nom',
            new_name='nom_loisir',
        ),
        migrations.RemoveField(
            model_name='loisir',
            name='adresse_1',
        ),
        migrations.RemoveField(
            model_name='loisir',
            name='id',
        ),
        migrations.RemoveField(
            model_name='loisir',
            name='saison',
        ),
        migrations.AddField(
            model_name='loisir',
            name='code_postal',
            field=models.IntegerField(default=12222, verbose_name='Code postale'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='loisir',
            name='description',
            field=models.TextField(default=22, verbose_name='Description du loisir'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='loisir',
            name='id_loisir',
            field=models.AutoField(default=2, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='loisir',
            name='name_voie',
            field=models.CharField(default=2, max_length=50, verbose_name='Nom de la voie'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='loisir',
            name='num_voie',
            field=models.IntegerField(default=2, verbose_name='Numéro de la voie'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='loisir',
            name='saisons',
            field=models.CharField(choices=[('ETE', 'Été'), ('HIVER', 'Hiver'), ('AUTOMNE', 'Automne'), ('PRINTEMPS', 'Printemps')], default=2, max_length=10, verbose_name='Saison'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='loisir',
            name='ville',
            field=models.CharField(default=2, max_length=50, verbose_name='Ville'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='AchetePack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_achat_pack', models.DateField(verbose_name="Date d'achat du pack")),
                ('nombre', models.IntegerField(validators=[MarseilleInsiderApp.models.validate_nombre_format], verbose_name='Nombre')),
                ('id_pack', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MarseilleInsiderApp.pack')),
                ('prix_client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MarseilleInsiderApp.client')),
            ],
        ),
        migrations.CreateModel(
            name='AcheteLoisir',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_achat_loisir', models.DateField(verbose_name="Date d'achat du loisir")),
                ('id_loisir', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MarseilleInsiderApp.loisir')),
                ('prix_client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MarseilleInsiderApp.client')),
            ],
        ),
        migrations.AddField(
            model_name='loisir',
            name='categorie',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='MarseilleInsiderApp.catégorie'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='loisir',
            name='id_fournisseur',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='MarseilleInsiderApp.fournisseur'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='loisir',
            name='prix_fournisseur',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='MarseilleInsiderApp.prix'),
            preserve_default=False,
        ),
    ]
