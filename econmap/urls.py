from django.urls import path
from econmap.views import base_view

urlpatterns = [
    path('', base_view, name='base')
]