from django.db import models

# Create your models here.

class Granth(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    edition = models.IntegerField()
    price = models.IntegerField()