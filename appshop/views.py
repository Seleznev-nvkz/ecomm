from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.conf import settings
from .models import Product, Category, OrderedProduct
# Create your views here.


def index(request):
    slider = Product.objects.filter(slider=True)
    product = Product.objects.filter(in_stock=True)
    category = Category.objects.all()
    context = {'products': product,
               'sliders': slider,
               'categories': category}
    return render(request, 'index.html', context = context)


def about(request):
    return render(request, 'about.html')


def pay(request):
    return render(request, 'pay.html')


def contacts(request):
    return render(request, 'contacts.html')


def delivering(request):
    return render(request, 'delivering.html')


def add_cart(request, id, quantity=1):
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


    my_buffer_cart = request.session.get(settings.CART_SESSION_ID)
    product = Product.objects.get(id=id)
    if not my_buffer_cart:
        my_buffer_cart = {}
    if product.id not in my_buffer_cart:
        print('product.id ', product.id)
        my_buffer_cart.update({product.id: quantity})
    if request.method == 'POST':
        print('kek')
        # item_for_post = 'item-'+id
        # request.POST.get("title", "")
        asd = request.POST.get(id, '')
        print('POST -------------------------- ', asd)
        quantity = request.POST.get('item-' + id)
        my_buffer_cart.update({id: quantity})
    new = {}
    try:
        for id, quantity in my_buffer_cart.items():
            print('buffercart', id, quantity)
            product = get_object_or_404(Product, id=id)
            new[product]['quantity'] = quantity
            print(new[product])
    except Exception as e:
        print(e)
    request.session[settings.CART_SESSION_ID] = my_buffer_cart
    request.session.modified = True
    context = {'news': new, 'my_buffer_cart': my_buffer_cart}
    return render(request, 'cart.html', context=context)


def show_cart(request):
    #del request.session[settings.CART_SESSION_ID]
    my_buffer_cart = request.session.get(settings.CART_SESSION_ID)
    new = {}
    if not my_buffer_cart:
        my_buffer_cart = {}
        # my_buffer_cart = request.session.get(settings.CART_SESSION_ID)
    else:
        product_ids = my_buffer_cart
        new = Product.objects.filter(id__in=product_ids)
    context = {'news': new}
    print('context ', context)
    return render(request, 'cart.html', context=context)


def item(request, id):
    product = Product.objects.get(id=id)
    category = Category.objects.all()
    context = {'products': product,
               'categories': category}
    return render(request, 'item.html', context=context)


def catalogue(request, cat):
    title_category = Category.objects.get(short_description=cat)
    product = Product.objects.filter(category=title_category)
    category = Category.objects.all()
    context = {'categories': category,
               'products': product,
               'title': title_category}
    return render(request, 'catalogue.html', context=context)


