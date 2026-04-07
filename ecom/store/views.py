from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

WOMEN_ITEMS = [
    {'id': 1, 'name': 'Summer Dress', 'description': 'Light and breezy summer dress', 'price': 45.99, 'image': 'products/summer_dress.jpeg'},
    {'id': 2, 'name': 'Denim Jacket', 'description': 'Classic denim jacket', 'price': 79.99,'image': 'products/denim_jacket.jpeg'},
    {'id': 3, 'name': 'Casual Blouse', 'description': 'Comfortable everyday blouse', 'price': 39.99,'image': 'products/casual_blouse.jpeg'},
]

MEN_ITEMS = [
    {'id': 1, 'name': 'Polo Shirt', 'description': 'Classic polo shirt', 'price': 34.99},
    {'id': 2, 'name': 'Canvas Jacket', 'description': 'Durable canvas jacket', 'price': 89.99},
    {'id': 3, 'name': 'Chino Pants', 'description': 'Comfortable chino pants', 'price': 54.99},
]

def home(request):
    return render(request, 'store/home.html')

def womens_clothing(request):
    return render(request, 'store/womens.html', {'items': WOMEN_ITEMS})

def mens_clothing(request):
    return render(request, 'store/mens.html', {'items': MEN_ITEMS})

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username and password:
            messages.success(request, f'Welcome, {username}!')
            request.session['cart'] = []
            return redirect('shop')
        else:
            messages.error(request, 'Please enter username and password.')
    return render(request, 'store/login.html')

def add_to_cart(request, item_id, category):
    if 'cart' not in request.session:
        request.session['cart'] = []
    
    items = WOMEN_ITEMS if category == 'women' else MEN_ITEMS
    item = next((i for i in items if i['id'] == item_id), None)
    
    if item:
        cart_item = {'id': item_id, 'name': item['name'], 'price': item['price'], 'qty': 1, 'category': category}
        request.session['cart'].append(cart_item)
        request.session.modified = True
        messages.success(request, f'{item["name"]} added to cart!')
    
    return redirect('cart')

def remove_from_cart(request, item_id):
    if 'cart' in request.session:
        request.session['cart'] = [item for item in request.session['cart'] if item['id'] != item_id]
        request.session.modified = True
    return redirect('cart')

def cart_page(request):
    cart = request.session.get('cart', [])
    total = sum(item['price'] * item['qty'] for item in cart)
    return render(request, 'store/cart.html', {'cart': cart, 'total': total})
