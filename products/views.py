from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone

# Create your views here.
from .models import Product

def home_view(request):

    product = Product.objects
    context = {
        'product' : product
    }
    return render(request, 'products/home.html', context)

# @login_required(login_url='/accounts/signup')
# def create_product_view(request):
#     if request.method == 'POST':
#         if request.POST['title'] and request.POST['body'] and request.POST['url'] and request.FILES['icon'] and request.FILES['image']:
#             product = Product()
#             product.title = request.POST['title']
#             product.body = request.POST['body']
#
#             if request.POST['url'].startswith('https://'):
#                 product.url = request.POST['url']
#             else:
#                 product.url = 'http://' + request.POST['url']
#
#             product.icon = request.FILES['icon']
#             product.image = request.FILES['image']
#             product.pub_date = timezone.datetime.now()
#             product.hunter = request.user
#             product.save()
#             return redirect('/products/' + str(product.id))
#
#         else:
#             return render(request, 'products/create_product.html', {'error':'Please enter all fields.'})
#
#     else:
#         return render(request, 'products/create_product.html')

@login_required(login_url="/accounts/signup")
def create(request):
    if request.method == 'POST':
        if request.POST['title'] and request.POST['body'] and request.POST['url'] and request.FILES['icon'] and request.FILES['image']:
            product = Product()
            product.title = request.POST['title']
            product.body = request.POST['body']
            if request.POST['url'].startswith('http://') or request.POST['url'].startswith('https://'):
                product.url = request.POST['url']
            else:
                product.url = 'http://' + request.POST['url']
            product.icon = request.FILES['icon']
            product.image = request.FILES['image']
            product.pub_date = timezone.datetime.now()
            product.hunter = request.user
            product.save()
            return redirect('/products/' + str(product.id))
        else:
            return render(request, 'products/create.html',{'error':'All fields are required.'})
    else:
        return render(request, 'products/create.html')



#if request.POST['title'] and request.POST['body'] and request.POST['url'] and request.FILES['icon'] and request.FILES['image']:
