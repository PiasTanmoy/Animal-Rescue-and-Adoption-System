from django.db import models

# Create your models here.

class Normaluser(models.Model):
    name = models.CharField(max_length=100)
    phone_no = models.IntegerField()
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.name


