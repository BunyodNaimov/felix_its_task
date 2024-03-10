from django.contrib import admin

from products.models import Product, Material, ProductMaterial, Warehouse, Order, OrderItem


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'code')


@admin.register(Material)
class IngredientsAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(ProductMaterial)
class ProductIngredientAdmin(admin.ModelAdmin):
    list_display = ('product', 'material', 'quantity')


@admin.register(Warehouse)
class WarehouseAdmin(admin.ModelAdmin):
    list_display = ('material', 'price', 'remainder')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('product', 'quantity', 'total_price', 'created_at')


@admin.register(OrderItem)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('warehouse', 'quantity', 'quantity', 'price')
