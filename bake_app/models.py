from django.db import models
from django.contrib.auth.models import AbstractUser

# Extending User Model
class User(AbstractUser):
    is_admin = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)

# Ingredient Model
class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    cost = models.DecimalField(max_digits=6, decimal_places=2)  # Cost per unit
    quantity = models.DecimalField(max_digits=10, decimal_places=2)  # Available quantity

    def __str__(self):
        return self.name

# BakeryItem Model
class BakeryItem(models.Model):
    name = models.CharField(max_length=100)
    cost_price = models.DecimalField(max_digits=6, decimal_places=2)
    selling_price = models.DecimalField(max_digits=6, decimal_places=2)
    ingredients = models.ManyToManyField(Ingredient, through='BakeryItemIngredient')

    def __str__(self):
        return self.name

# BakeryItemIngredient Model
class BakeryItemIngredient(models.Model):
    bakery_item = models.ForeignKey(BakeryItem, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity_percentage = models.DecimalField(max_digits=5, decimal_places=2)  # Percent of the ingredient in the bakery item

# Order Model
class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)

# OrderItem Model
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    bakery_item = models.ForeignKey(BakeryItem, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    @property
    def get_total(self):
        return self.bakery_item.selling_price * self.quantity
