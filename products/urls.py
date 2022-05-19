from django.urls import path

from products.views import dynamic_lookup_view, product_create_view

urlpatterns = [
    path('<int:id>/', dynamic_lookup_view, name='product'),
]
