# Generated by Django 4.0.3 on 2022-05-17 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0024_pg001_pg001identifiant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pg003',
            name='pg003estbloque',
            field=models.BooleanField(default=True, verbose_name='Bloquer le compte'),
        ),
    ]