from django.shortcuts import render

# Create your views here.
from .models import Product

def home_view(request):

    product = Product.objects
    context = {
        'product' : product
    }
    return render(request, 'products/home.html', context)
