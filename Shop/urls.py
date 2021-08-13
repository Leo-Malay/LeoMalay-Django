from django.urls import path
import Shop.views as views

urlpatterns = [
    path('', views.index, name='index'),
    path('cart', views.cart, name='cart'),
    path('product', views.product, name='product'),
    path('order', views.order, name='order'),
]
