from django.urls import path
from econmap.views import base_view,product_view,category_view

urlpatterns = [
    path('product/<product_slug>', product_view, name='product_detail'),
    path('category/<category_slug>', category_view, name='category_detail'),
    path('', base_view, name='base')
]