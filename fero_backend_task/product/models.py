from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    weight = models.DecimalField(
        max_digits=4,
        decimal_places=2,
    )
