# Generated by Django 4.0.3 on 2022-05-11 02:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_ps003_ps003morant'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pg101',
            name='ps003code',
        ),
        migrations.RemoveField(
            model_name='ps003',
            name='pg001_id',
        ),
        migrations.RemoveField(
            model_name='ps003',
            name='pg002_id',
        ),
        migrations.DeleteModel(
            name='Pg100',
        ),
        migrations.DeleteModel(
            name='Pg101',
        ),
        migrations.DeleteModel(
            name='Ps003',
        ),
    ]
