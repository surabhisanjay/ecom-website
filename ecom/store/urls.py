from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_page, name='home'),
    path('shop/', views.home, name='shop'),
    path('women/', views.womens_clothing, name='women'),
    path('men/', views.mens_clothing, name='men'),
    path('login/', views.login_page, name='login'),
    path('cart/', views.cart_page, name='cart'),
    path('add-to-cart/<int:item_id>/<str:category>/', views.add_to_cart, name='add_to_cart'),
    path('remove-from-cart/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
]
