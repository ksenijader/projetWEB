# Generated by Django 4.1 on 2023-11-16 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MarseilleInsiderApp', '0005_alter_catégorie_categorie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loisir',
            name='saisons',
            field=models.CharField(choices=[('ETE', 'Été'), ('HIVER', 'Hiver'), ('AUTOMNE', 'Automne'), ('PRINTEMPS', 'Printemps'), ('TA', 'Toutes saisons')], max_length=10, verbose_name='Saison'),
        ),
    ]
