from django.shortcuts import render
from .models import Products


def list_products(request):
    products = Products.objects.all()
    context = {
        'products': products
    }

    return render(request, 'products/list.html', context=context)
