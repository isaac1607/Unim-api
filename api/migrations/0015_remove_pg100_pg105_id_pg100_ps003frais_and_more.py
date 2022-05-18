# Generated by Django 4.0.3 on 2022-05-16 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_remove_ps110_ps110code_remove_ps110_ps110imei_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pg100',
            name='pg105_id',
        ),
        migrations.AddField(
            model_name='pg100',
            name='ps003frais',
            field=models.FloatField(default=0, verbose_name='Frais'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pg100',
            name='pg100somme',
            field=models.FloatField(verbose_name='solde_envoye'),
        ),
        migrations.DeleteModel(
            name='Pg105',
        ),
    ]
