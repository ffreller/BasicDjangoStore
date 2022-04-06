from django.urls import path
from customers.views import customer_create_view, customer_detail_view_dynamic, customer_delete_view, customer_list_view, customer_update_view

app_name = 'customers'
urlpatterns = [
    path('detail/<int:id>/', customer_detail_view_dynamic, name='customer_detail'),
    path('delete/<int:id>/', customer_delete_view, name='customer_delete'),
    path('update/<int:id>/', customer_update_view, name='customer_update'),
    path('create/', customer_create_view, name='customer_create'),
    path('list/', customer_list_view, name='customer_list'),
    path('', customer_list_view, name='customer_list'),
]