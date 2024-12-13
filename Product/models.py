
from django.db import models

from django.contrib.auth.models import User


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255,null=True)
    image = models.ImageField(null=True,blank=True,upload_to='image/')
    date = models.DateField(max_length=255)
    location = models.CharField(max_length=255,null=True)
    type= models.CharField(max_length=255,null=True)


    def __str__(self):
        return self.name


class Venue(models.Model):
    name = models.CharField('Venue Name',max_length=120,)
    address = models.CharField(max_length=300)
    zip_code = models.CharField('Zip Code',max_length=15)
    phone = models.CharField('Contact Phone',max_length=25,blank=True)
    web = models.URLField('Website Address',blank=True)
    email_address = models.EmailField('Email Address',blank=True)

    def __str__(self):
        return self.name










