from django.urls import reverse
from django.db import models
from customers.models import Customer
from products.models import Product


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)    
    def get_absolute_url(self):
        return reverse("orders:order_detail", kwargs={'id':self.id})
        # return f'/products:detail/{self.id}/'
    