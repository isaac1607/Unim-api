# Generated by Django 4.0.3 on 2022-05-17 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0021_pg001_pg001secteur_pg001_pg001type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pg003',
            name='pg003mdp',
            field=models.CharField(max_length=200, verbose_name='Mot de passe'),
        ),
        migrations.AlterField(
            model_name='pg003',
            name='pg003plafond',
            field=models.IntegerField(default=0, verbose_name='Plafond'),
        ),
    ]