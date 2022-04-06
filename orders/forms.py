from django import forms
from customers.models import Customer
from products.models import Product

class OrderForm(forms.Form):
    customer_id = forms.IntegerField()
    product_choices = Product.objects.all().values_list('id', 'title')
    # product_choices = ((product.id, product.title) for product in product_choices)
    products_ids = forms.MultipleChoiceField(choices=product_choices, widget=forms.SelectMultiple(attrs={
        'size':10,
        }))
    class Meta:
        fields = [
            "customer_id",
            "products_ids",
        ]
    
    
    def clean_customer_id(self, *args, **kwargs):
        customer_id = self.cleaned_data['customer_id']
        queryset_customer = Customer.objects.filter(id=customer_id)
        if len(queryset_customer) == 0:
            raise forms.ValidationError("Customer does not exist")
        return customer_id

    
    def clean_products_ids(self, *args, **kwargs):
        products_ids = self.cleaned_data['products_ids']
        if len(products_ids) == 0:
            raise forms.ValidationError("You must select at least one product")
        return products_ids
