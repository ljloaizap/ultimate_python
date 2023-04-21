from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255)


class Product(models.Model):
    name = models.CharField(max_length=255)
    stock = models.IntegerField()
    score = models.FloatField()
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )
