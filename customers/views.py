from django.shortcuts import render, get_object_or_404, redirect
from django.forms.models import model_to_dict
from .models import Customer
from .forms import CustomerForm

# Create your views here.
def customer_detail_view_dynamic(request, id):
    obj = get_object_or_404(Customer, id=id)
    context = {
        'object': obj
    }
    return render(request, "customers/customer_detail.html", context)

def customer_list_view(request):
    queryset = Customer.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, "customers/customer_list.html", context)


def customer_create_view(request):
    form = CustomerForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = CustomerForm()
    context = {
        'form': form
    }
    return render(request, "customers/customer_create.html", context)


def customer_delete_view(request, id):
    obj = get_object_or_404(Customer, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect('../../')
    context = {
        'object': obj
    }
    return render(request, "customers/customer_delete.html", context)


def customer_update_view(request, id):
    obj = Customer.objects.get(id=id)
    initial_data = model_to_dict(obj)
    form = CustomerForm(request.POST or None, initial = initial_data, instance=obj)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request, "products/product_update.html", context)


