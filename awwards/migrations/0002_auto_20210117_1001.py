# Generated by Django 3.1.5 on 2021-01-17 08:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('awwards', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='profile_image',
            new_name='project_image',
        ),
    ]
