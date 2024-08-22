
from django.db import models

class Product(models.Model):
    category = models.CharField(max_length=255, null=True, blank=True)
    url = models.URLField(max_length=500, null=True, blank=True)
    title = models.CharField(max_length=255, null=True, blank=True)
    last_7_day_sale = models.CharField(max_length=100, null=True, blank=True)
    available_skus = models.JSONField(null=True, blank=True)  # Use JSONField for complex data
    fit = models.CharField(max_length=100, null=True, blank=True)
    fabric = models.CharField(max_length=255, null=True, blank=True)
    neck = models.CharField(max_length=100, null=True, blank=True)
    sleeve = models.CharField(max_length=100, null=True, blank=True)
    pattern = models.CharField(max_length=100, null=True, blank=True)
    length = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)  # TextField for longer text
    image_url = models.URLField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.title
