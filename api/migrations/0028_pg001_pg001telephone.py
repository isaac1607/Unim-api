# Generated by Django 4.0.3 on 2022-05-17 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0027_ps111_pg003_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='pg001',
            name='pg001telephone',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Retrait'),
        ),
    ]