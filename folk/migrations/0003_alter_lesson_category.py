# Generated by Django 5.0.4 on 2024-04-18 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('folk', '0002_lesson_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='category',
            field=models.CharField(max_length=150),
        ),
    ]