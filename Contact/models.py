from django.db import models

# Create your models here.
class Contact(models.Model):
    Name = models.CharField(max_length=255,null=True)
    Email = models.CharField(max_length=255,null=True)
    Phone = models.CharField(max_length=255,null=True)
    Reason = models.CharField(max_length=255,null=True)
    Comment = models.CharField(max_length=255,null=True)



    def __str__(self):
        return self.Name



