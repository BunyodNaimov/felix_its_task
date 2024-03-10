from django.db import models

from .base import BaseModel


class Order(BaseModel):
    product = models.ForeignKey("Product", on_delete=models.CASCADE, related_name='orders')
    quantity = models.IntegerField(default=0)
    total_price = models.FloatField(default=0)


class OrderItem(BaseModel):
    warehouse = models.ForeignKey("Warehouse", on_delete=models.SET_NULL, related_name='orders', null=True)
    quantity = models.PositiveIntegerField(default=0)
    price = models.FloatField(null=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items', null=True)

    def save(self, *args, **kwargs):
        self.price = self.warehouse.price if self.warehouse else None
        super().save(*args, **kwargs)
