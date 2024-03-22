from django.contrib import admin
from .models import *

class FoodAdmin(admin.ModelAdmin):
    list_display = ( "food_id", "food_name", "price", "image")
    search_fields = ("food_name", )
    list_filter = ("food_name", "price", )
admin.site.register(Food, FoodAdmin)

admin.site.register(Category)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(CustomUser)
