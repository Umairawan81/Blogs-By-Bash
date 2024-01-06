from django.db import models
from tinymce.models import HTMLField


class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.TextField()
    

class Post(models.Model):
    title = models.CharField(max_length=255)
    tag = models.CharField(max_length=50)
    description = HTMLField()
    auther = models.CharField(max_length=50)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return self.title
    
class Comments(models.Model):
    post = models.ForeignKey(Post , on_delete= models.CASCADE , null=True)
    cmt = models.TextField()
    name = models.CharField(max_length=50 , default="Anonymous")
    date_cmt = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_cmt']
