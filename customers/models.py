from django.urls import reverse
from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=120) # max_length = required
    email = models.EmailField(blank=True, null=True)
    age = models.IntegerField()
    about_me = models.TextField(blank=True, null=True)
    
    def get_absolute_url(self):
        return reverse("customers:customer_detail", kwargs={'id':self.id})