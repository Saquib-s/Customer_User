from django.db import models


# Create your models here.
class user(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    mobile_no = models.IntegerField(unique=True)


class Customer(models.Model):
    profile_no = models.OneToOneField(user, on_delete=models.CASCADE, null=True, blank=True)
