from django.db import models

# Create your models here.
class Post1(models.Model):
    title= models.CharField(max_length=200)
    body=models.TextField()
    author = models.ForeignKey("auth.User", on_delete= models.CASCADE)