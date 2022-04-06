from django.urls import path
from products.views import product_create_view, product_detail_view_dynamic, product_delete_view, product_list_view, product_update_view

app_name = 'products'
urlpatterns = [
    path('detail/<int:id>/', product_detail_view_dynamic, name='product_detail'),
    path('delete/<int:id>/', product_delete_view, name='product_delete'),
    path('update/<int:id>/', product_update_view, name='product_update'),
    path('create/', product_create_view, name='product_create'),
    path('list/', product_list_view, name='product_list'),
    path('', product_list_view, name='product_list'),
]