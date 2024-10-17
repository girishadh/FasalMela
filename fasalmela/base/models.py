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
    listedAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title


class Orders(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    orderedAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    total = models.FloatField()
    status = models.BooleanField(default=False)
    def __str__(self):
        return self.user.username
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    orders = models.ManyToManyField(Orders)
    seller = models.BooleanField(default=False)
    def __str__(self):
        return self.user.username
    