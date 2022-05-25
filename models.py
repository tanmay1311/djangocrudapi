from django.db import models
from sklearn import tree


class Item(models.Model):
    name = models.CharField(max_length=255,null=True,blank=True)
    username = models.CharField(max_length=255,null=True,blank=True)
    age = models.PositiveIntegerField(null=True,blank=True)
    dob = models.CharField(max_length=255,null=True,blank=True)
  
    def __str__(self) -> str:
        return self.name
