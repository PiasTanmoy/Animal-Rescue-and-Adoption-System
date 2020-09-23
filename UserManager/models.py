from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    first_name = models.CharField(max_length=20)
    middle_name = models.CharField(max_length=20, blank=True)
    last_name = models.CharField(max_length=20)
    street = models.CharField(max_length=35)
    city = models.CharField(max_length=25)
    post_code = models.CharField(max_length=5)
    nid_no = models.CharField(max_length=17)
    phone_no = models.CharField(max_length=11)
    profile_pic = models.ImageField(upload_to='uploads/user', blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
