# Generated by Django 4.0.3 on 2022-05-16 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0018_retrait_alter_ps003_ps003numero_compte_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pg002',
            name='pg002ps',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='ps'),
        ),
    ]
