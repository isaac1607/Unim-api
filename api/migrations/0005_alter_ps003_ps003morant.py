# Generated by Django 4.0.3 on 2022-05-08 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_remove_pg002_pg002numeroz'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ps003',
            name='ps003morant',
            field=models.FloatField(default=0, verbose_name='Morant'),
        ),
    ]
