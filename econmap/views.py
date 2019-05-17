
from django.shortcuts import render
from econmap.models import Category,Product

# Create your views here.

def base_view(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    context = {
        'categries': categories,
        'products': products,
    }
    return render(request, 'base.html', context)