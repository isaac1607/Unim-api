# Generated by Django 4.0.3 on 2022-05-17 20:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0026_remove_ps111_pg002_id_remove_ps111_ps111code_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ps111',
            name='pg003_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.RESTRICT, to='api.pg003', verbose_name='Business'),
            preserve_default=False,
        ),
    ]
