from django.contrib import admin
from .models import BakeryItem,BakeryItemIngredient,Order,OrderItem,User,Ingredient

admin.site.register(BakeryItem),
admin.site.register(BakeryItemIngredient),
admin.site.register(Order),
admin.site.register(OrderItem),
admin.site.register(User),
admin.site.register(Ingredient),
