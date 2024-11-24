
from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255,null=True)
    image = models.ImageField(null=True,blank=True,upload_to='image/')
    date = models.DateField(max_length=255)
    location = models.CharField(max_length=255,null=True)
    type= models.CharField(max_length=255,null=True)





    def __str__(self):
        return self.name





