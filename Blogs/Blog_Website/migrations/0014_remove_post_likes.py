# Generated by Django 4.2.7 on 2024-01-20 09:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog_Website', '0013_delete_user_alter_post_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='likes',
        ),
    ]
