# Generated by Django 4.0.3 on 2022-05-11 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_pg002_pg002timeessai'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pg002',
            name='pg002essai',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Temps expiration'),
        ),
        migrations.AlterField(
            model_name='pg002',
            name='pg002timeessai',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Temps essaie'),
        ),
    ]
