from django.contrib import admin
from .models import Product , Location ,Family ,Transaction 

# Register your models here.

admin.site.register(Product)
admin.site.register(Location)
admin.site.register(Family)
admin.site.register(Transaction)