from django.db import models

# Create your models here.
class Animal(models.Model):
    category = models.CharField(max_length=30)
    species = models.CharField(max_length=30)
    