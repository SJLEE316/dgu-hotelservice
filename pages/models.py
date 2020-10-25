from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=50, null=False)
    menu = models.CharField(max_length=50, null=False, default="")
    chef = models.CharField(max_length=50, default="")
    content = models.TextField()
    image = models.ImageField(upload_to='images/', null=True)


