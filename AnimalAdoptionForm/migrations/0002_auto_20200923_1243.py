# Generated by Django 3.1.1 on 2020-09-23 06:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AnimalAdoptionForm', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='Adoption',
        ),
    ]
