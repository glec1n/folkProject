# Generated by Django 5.0.4 on 2024-04-19 18:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('folk', '0005_image'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Image',
            new_name='ImageHolder',
        ),
    ]