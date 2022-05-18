# Generated by Django 4.0.3 on 2022-05-17 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0020_remove_pg001_pg103_id_remove_pg001_pg104_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='pg001',
            name='pg001secteur',
            field=models.CharField(choices=[('TRANSPORT', 'TRANSPORT'), ('INDUSTRIE', 'INDUSTRIE'), ('FINANCE', 'FINANCE'), ('SANTE', 'SANTE'), ('TIC', 'TIC'), ('AUTRES', 'AUTRES')], default='AUTRES', max_length=200, verbose_name='Secteur'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pg001',
            name='pg001type',
            field=models.CharField(choices=[('SI', 'SOCIETE INDIVIDUELLE'), ('SARL', 'SARL'), ('SA', 'SA'), ('AUTRES', 'AUTRES')], default='AUTRES', max_length=200, verbose_name='Type'),
            preserve_default=False,
        ),
    ]
