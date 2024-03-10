from django.db import models


class Warehouse(models.Model):
    material = models.ForeignKey("Material", on_delete=models.CASCADE, related_name='warehouse')
    price = models.FloatField(default=0)
    remainder = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.material.name} - {self.price} - {self.remainder}"
