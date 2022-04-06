from django.urls import path
# from orders.views import order_create_view, order_detail_view_dynamic, order_delete_view, order_list_view, order_update_view
from orders.views import order_detail_view_dynamic, order_create_view, order_delete_view, order_list_view, order_update_view

app_name = 'orders'
urlpatterns = [
    path('', order_list_view, name='order_list'),
    path('list/', order_list_view, name='order_list'),
    path('detail/<int:id>/', order_detail_view_dynamic, name='order_detail'),
    path('delete/<int:id>/', order_delete_view, name='order_delete'),
    path('update/<int:id>/', order_update_view, name='order_update'),
    path('create/', order_create_view, name='order_create'),

]