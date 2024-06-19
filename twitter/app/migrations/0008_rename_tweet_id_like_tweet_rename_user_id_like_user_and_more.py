# Generated by Django 5.0.3 on 2024-06-19 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_profile_bio'),
    ]

    operations = [
        migrations.RenameField(
            model_name='like',
            old_name='tweet_id',
            new_name='tweet',
        ),
        migrations.RenameField(
            model_name='like',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='reply',
            old_name='tweet_id',
            new_name='tweet',
        ),
        migrations.RenameField(
            model_name='reply',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='tweet',
            old_name='user_id',
            new_name='user',
        ),
        migrations.AlterField(
            model_name='tweet',
            name='tweet',
            field=models.TextField(default=''),
        ),
    ]