from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from Shop.models import Product


def index(request):
    data = list(Product.objects.all())
    return render(request, "shop/home.html", {'title': 'Shop', 'data': data})


def cart(request):
    return render(request, "shop/cart.html", {})


def product(request):
    if request.GET:
        try:
            p_id = request.GET['id']
            try:
                data = list(Product.objects.get(id=p_id))
                return render(request, "shop/product.html", {'title': p_id, 'data': data})
            except:
                return index(request)
        except:
            return index(request)


def order(request):
    return render(request, "shop/order.html", {})
