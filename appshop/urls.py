from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/', views.about, name='about'),
    url(r'^pay/', views.pay, name='pay'),
    url(r'^delivering/', views.delivering, name='delivering'),
    url(r'^contacts/', views.contacts, name='contacts'),
    url(r'^cart/$', views.show_cart, name='cart'),
    url(r'^cart/(?P<id>[0-9]+)/$', views.add_cart, name='itemtocart'),
    url(r'^item/(?P<id>[0-9]+)/$', views.item, name='item'),
    url(r'^catalogue/(?P<cat>\w+)/$', views.catalogue, name='catalogue')
]