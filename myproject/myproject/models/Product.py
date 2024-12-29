from django.db import models
from .User import User

class Product(models.Model):
    name = models.CharField(max_length=50)
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.FloatField()
    description = models.CharField(max_length=255)
    stock = models.IntegerField()
