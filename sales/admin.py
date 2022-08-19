from django.contrib import admin
from .models import Products, Sold

class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('product_name',)}

#admin.site.register([Products, Sold]) #to group more than 2 objects
#admin.site.register(Products) #to include only one object
admin.site.register(Sold)
admin.site.register(Products, ProductsAdmin)
