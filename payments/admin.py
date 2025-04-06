from django.contrib import admin
from payments.models import Cart, CartItem,Purchase,PurchaseItem
# Register your models here.


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['id', 'user']


@admin.register(Purchase)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'status']


admin.site.register(CartItem)
admin.site.register(PurchaseItem)