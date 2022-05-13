from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    age = models.PositiveIntegerField()
    dob = models.CharField(max_length=255)
  
    def __str__(self) -> str:
        return self.name
