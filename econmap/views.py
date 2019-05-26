
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

def product_view(request, product_slug):
    product = Product.objects.get(slug=product_slug)
    categories = Category.objects.all()
    context = {
        'product': product,
        'categries': categories
    }
    return render(request, 'product.html', context)

def category_view(request, category_slug):
    categories = Category.objects.all()
    category = Category.objects.get(slug=category_slug)
    products_of_category = Product.objects.filter(category=category)
    context = {
        'category': category,
        'products_of_category': products_of_category,
        'categries': categories
    }
    return render(request, 'category.html', context)