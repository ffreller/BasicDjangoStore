from django.urls import reverse
from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=120) # max_length = required
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    active = models.BooleanField(default=True)
    
    def get_absolute_url(self):
        return reverse("products:product_detail", kwargs={'id':self.id})
        # return f'/products:detail/{self.id}/'
    