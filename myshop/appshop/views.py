from django.shortcuts import render
from .models import Product, Category, OrderedProduct
# Create your views here.


def index(request):
    product = Product.objects.filter(is_enabled=True)
    category = Category.objects.all()
    context = {'products': product,
               'categories': category}
    return render(request, 'index.html', context=context)


def about(request):
    return render(request, 'about.html')


def cart(request, id="1"):
    product = Product.objects.get(id=id)
    ordered_product = OrderedProduct.objects.filter(product__id=id)
    context = {'ordered_products': ordered_product}
    if id is True:
        cart[id] = Product.objects.get(id=id)
        request.session['cart'] = cart
    cart = request.session.get('cart', {})
    return render(request, 'cart.html', context=context)


def item(request, id):
    product = Product.objects.get(id=id)
    category = Category.objects.all()
    context = {'products': product,
               'categories': category}
    return render(request, 'item.html', context=context)


def catalogue(request, cat):
    category = Category.objects.get(name=cat)
    product = Product.objects.filter(category=category)
    category = Category.objects.all()
    context = {'categories': category,
               'products': product}
    return render(request, 'catalogue.html', context=context)


