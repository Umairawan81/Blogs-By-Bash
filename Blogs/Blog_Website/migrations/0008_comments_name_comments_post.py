# Generated by Django 4.2.7 on 2023-11-20 18:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Blog_Website', '0007_alter_comments_cmt'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='name',
            field=models.CharField(default='Anonymous', max_length=50),
        ),
        migrations.AddField(
            model_name='comments',
            name='post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='Blog_Website.post'),
        ),
    ]
