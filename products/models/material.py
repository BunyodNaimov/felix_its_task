from django.db import models


class Material(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class ProductMaterial(models.Model):
    product = models.ForeignKey("Product", on_delete=models.CASCADE, related_name='materials')
    material = models.ForeignKey(Material, on_delete=models.CASCADE, related_name='products')
    quantity = models.FloatField(default=0)

    def __str__(self):
        return f"{self.product.name} - {self.material.name} - {self.quantity}"