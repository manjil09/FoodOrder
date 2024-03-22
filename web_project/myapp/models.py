from email.policy import default
from enum import unique
from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    bio = models.CharField(max_length=255, blank=True)
    register_date = models.DateField(auto_now_add=True)#not necessary AbstracUser provides a default date_joined

class Food(models.Model):
    food_id = models.AutoField(primary_key=True)
    food_name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True)
    image = models.ImageField(upload_to='food_images/')
    variety_options = models.CharField(max_length=255)
    category_id = models.ForeignKey('Category', on_delete=models.CASCADE)

    def __str__ (self):
        return self.food_name

# class VarietyOption(models.Model):
#     variety_id = models.AutoField(primary_key=True)
#     variety_name = models.CharField(max_length=100)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     food = models.ForeignKey(Food, related_name='variety_options', on_delete=models.CASCADE)

class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=50, unique = True)
    
    def __str__ (self):
        return self.category_name

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey('CustomUser', on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.BooleanField(default=False)

class OrderItem(models.Model):
    order_item_id = models.AutoField(primary_key=True)
    order_id = models.ForeignKey('Order', on_delete=models.CASCADE)
    food_id = models.ForeignKey('Food', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)

