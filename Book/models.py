from django.db import models

# Create your models here.

class Kitab(models.Model):
    title = models.CharField(max_length=100)
    price = models.IntegerField()
    author = models.CharField(max_length=100)
    edition = models.IntegerField()