from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
class Item(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    category = models.ManyToManyField(Category)
    label = models.CharField(max_length=100)
    description = models.TextField()
    listedBy = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title