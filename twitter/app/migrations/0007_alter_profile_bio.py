# Generated by Django 5.0.3 on 2024-06-18 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_profile_bio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(blank=True, default='', null=True),
        ),
    ]
