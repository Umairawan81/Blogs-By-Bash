# Generated by Django 4.2.7 on 2023-11-20 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog_Website', '0006_alter_comments_cmt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='cmt',
            field=models.TextField(),
        ),
    ]
