from django.db import models
from django.utils import timezone

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'categories'


class Product(models.Model):
    name = models.CharField(max_length=255)
    stock = models.IntegerField()
    score = models.FloatField()
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(default=timezone.now)
