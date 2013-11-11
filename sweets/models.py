from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='products')
    candies = models.TextField(max_length=100)
    height = models.IntegerField()
    width = models.IntegerField()
    pre_order = models.CharField(max_length=100)
    price = models.IntegerField()
