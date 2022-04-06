from django.shortcuts import render, get_object_or_404, redirect
from django.forms.models import model_to_dict
from .models import Order
from customers.models import Customer
from products.models import Product
from .forms import OrderForm

# Create your views here.
def order_detail_view_dynamic(request, id):
    obj = get_object_or_404(Order, id=id)
    context = {
        'object': obj
    }
    return render(request, "orders/order_detail.html", context)


def order_list_view(request):
    queryset = Order.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, "orders/order_list.html", context)


def order_create_view(request):
    form = OrderForm(request.POST or None)
    if form.is_valid():
        customer_id = form.cleaned_data['customer_id']
        customer = Customer.objects.get(id=customer_id)
        products_ids = form.cleaned_data['products_ids']
        order = Order.objects.create(customer=customer)
        for product_id in products_ids:
            print(product_id)
            product = Product.objects.get(id=product_id)
            order.products.add(product)
        order.save()
    context = {
        'form': form
    }
    return render(request, "orders/order_create.html", context)


def order_delete_view(request, id):
    obj = get_object_or_404(Order, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect('../../')
    context = {
        'object': obj
    }
    return render(request, "orders/order_delete.html", context)



def order_update_view(request, id):
    order = Order.objects.get(id=id)
    product_choices = order.products.all().values_list('id', flat=True)
    print(product_choices)
    form = OrderForm(request.POST or None, initial = {
        'customer_id': order.customer.id,
        'products_ids': [cat for cat in product_choices]
        })
    if form.is_valid():
        customer_id = form.cleaned_data['customer_id']
        customer = Customer.objects.get(id=customer_id)
        products_ids = form.cleaned_data['products_ids']
        order.customer = customer
        order.products.clear()
        for product_id in products_ids:
            print(product_id)
            product = Product.objects.get(id=product_id)
            order.products.add(product)
        order.save()
    context = {
        'form': form
    }
    return render(request, "orders/order_update.html", context)
