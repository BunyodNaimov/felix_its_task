from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=150)
    code = models.PositiveIntegerField(unique=True)

    def __str__(self):
        return self.name

