from django.contrib import admin
from core.models import WorkshopRepair, Rating, Sale, Product, Order

# Register your models here.
admin.site.register(WorkshopRepair)
admin.site.register(Rating)
admin.site.register(Sale)
admin.site.register(Product)
admin.site.register(Order)