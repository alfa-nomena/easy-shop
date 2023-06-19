from django.db import models

class Product(models.Model):
    category= models.ForeignKey("Category", on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=2, decimal_places=0)

class Category(models.Model):
    name=models.CharField(max_length=50)