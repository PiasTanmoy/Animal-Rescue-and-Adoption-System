from django.db import models


# Create your models here.
class Adoption(models.Model):
    name = models.CharField(max_length=300)
    contact_no = models.IntegerField()
    present_address = models.CharField(max_length=500)
    nid_no = models.CharField(max_length=200)


    def __str__(self):
        return self.name