from django.db import models

class User(models.Model):
    username = models.CharField(max_length=50)
    title = models.CharField(max_length=50, choices=[('Mr', 'Mr'), ('Mrs', 'Mrs'), ('Ms', 'Ms')], default='Mr')
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    address = models.CharField(max_length=255, null=True)
    

class Product(models.Model):
    name = models.CharField(max_length=50)
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.FloatField()
    description = models.CharField(max_length=255)
    stock = models.IntegerField()


