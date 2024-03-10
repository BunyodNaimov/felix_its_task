from django.urls import path

from products.views import ProductOrderCreateView, ProductListView

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('orders/', ProductOrderCreateView.as_view(), name='orders'),
]
