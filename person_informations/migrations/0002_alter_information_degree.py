# Generated by Django 4.2.11 on 2024-03-21 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person_informations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='information',
            name='degree',
            field=models.CharField(choices=[('BAC', 'Baccalauréat'), ('BAC+2', 'Brevet de Technicien Supérieur'), ('BAC+3', 'license'), ('BAC+5', 'master'), ('BAC+8', 'doctorat')], default='BAC', max_length=50),
        ),
    ]
