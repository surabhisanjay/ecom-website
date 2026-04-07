from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from decimal import Decimal
from .models import Product, Order, OrderItem


def home(request):
    return render(request, 'store/home.html')

def womens_clothing(request):
    items = Product.objects.filter(category='women')
    return render(request, 'store/womens.html', {'items': items})

def mens_clothing(request):
    items = Product.objects.filter(category='men')
    return render(request, 'store/mens.html', {'items': items})

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
    
    try:
        product = Product.objects.get(id=item_id, category=category)
        cart_item = {
            'id': product.id,
            'name': product.name,
            'price': float(product.price),
            'qty': 1,
            'category': category
        }
        request.session['cart'].append(cart_item)
        request.session.modified = True
        messages.success(request, f'{product.name} added to cart!')
    except Product.DoesNotExist:
        messages.error(request, 'Product not found.')
    
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

def checkout_page(request):
    cart = request.session.get('cart', [])
    
    if not cart:
        messages.error(request, 'Your cart is empty!')
        return redirect('cart')
    
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        city = request.POST.get('city')
        postal_code = request.POST.get('postal_code')
        
        if full_name and email and phone and address and city and postal_code:
            total = sum(item['price'] * item['qty'] for item in cart)
            
            # Create order
            order = Order.objects.create(
                full_name=full_name,
                email=email,
                phone=phone,
                address=address,
                city=city,
                postal_code=postal_code,
                total_amount=Decimal(str(total)),
                status='confirmed'
            )
            
            # Create order items
            for item in cart:
                try:
                    product = Product.objects.get(id=item['id'])
                    OrderItem.objects.create(
                        order=order,
                        product=product,
                        quantity=item['qty'],
                        price=Decimal(str(item['price']))
                    )
                except Product.DoesNotExist:
                    pass
            
            messages.success(request, f'Thank you {full_name}! Order #{order.id} placed successfully. Total: ${total:.2f}')
            request.session['cart'] = []
            request.session.modified = True
            return redirect('shop')
        else:
            messages.error(request, 'Please fill in all fields.')
    
    total = sum(item['price'] * item['qty'] for item in cart)
    return render(request, 'store/checkout.html', {'cart': cart, 'total': total})
