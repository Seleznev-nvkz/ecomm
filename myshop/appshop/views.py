from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Product, Category, OrderedProduct
# Create your views here.


def index(request):
    product = Product.objects.filter(slider=True)
    category = Category.objects.all()
    context = {'products': product,
               'categories': category}
    return render(request, 'index.html', context=context)


def about(request):
    return render(request, 'about.html')


def cart(request, id=1):
    # product = Product.objects.get(id=id)
    #
    # cart = request.session.get('cart', {})
    # if id == :
    #     request.session[id] = quantity
    # ordered_product = OrderedProduct.objects.create(product=product)
    # context = {'carts': cart}
    # return render(request, 'cart.html', context=context)
    # cart = request.session.get('cart', {})
    # cart[item_id] = quantity
    # request.session['cart'] = cart
    quantity = 1
    my_buffer_cart = request.session.get('my_cart', {})
    if id not in my_buffer_cart:
        #request.session['my_cart'].items = (id:quantity)]
        #request.session['my_cart'] = {id: quantity}
        my_buffer_cart.update({id: quantity})
    new = {}
    for id, quantity in my_buffer_cart.items():
        new[get_object_or_404(Product, id=id)] = quantity
    context = {'news': new}
    return render(request, 'cart.html', context=context)



def item(request, id):
    product = Product.objects.get(id=id)
    category = Category.objects.all()
    context = {'products': product,
               'categories': category}
    return render(request, 'item.html', context=context)


def catalogue(request, cat):
    category = Category.objects.get(short_description=cat)
    product = Product.objects.filter(category=category)
    category = Category.objects.all()
    context = {'categories': category,
               'products': product}
    return render(request, 'catalogue.html', context=context)


