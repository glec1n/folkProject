# Generated by Django 5.0.4 on 2024-06-03 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('folk', '0015_rename_comment_comment_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='image',
            field=models.ImageField(default=1, upload_to='images'),
            preserve_default=False,
        ),
    ]
