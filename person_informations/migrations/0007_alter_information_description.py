# Generated by Django 4.2.11 on 2024-03-25 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person_informations', '0006_information_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='information',
            name='description',
            field=models.TextField(blank=True, default='', max_length=1000, verbose_name='A propos de moi'),
        ),
    ]
