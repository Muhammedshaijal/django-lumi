from django.db import models

# Create your models here.
class Books(models.Model):
    name=models.CharField()
    author=models.CharField()
    price=models.PositiveIntegerField()
    publisher=models.CharField()