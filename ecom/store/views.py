from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from decimal import Decimal
from .models import Product, Order, OrderItem


# ---------------- HOME ----------------
def home(request):
    return render(request, 'store/home.html')


def womens_clothing(request):
    items = Product.objects.filter(category='women')
    return render(request, 'store/womens.html', {'items': items})


def mens_clothing(request):
    items = Product.objects.filter(category='men')
    return render(request, 'store/mens.html', {'items': items})


# ---------------- LOGIN ----------------
def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome {username}!')
            return redirect('shop')
        else:
            messages.error(request, 'Invalid username or password')

    return render(request, 'store/login.html')


# ---------------- SIGNUP ----------------
def signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if not username or not email or not password:
            messages.error(request, "All fields are required")
            return redirect('signup')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect('signup')

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        messages.success(request, "Account created! Please login.")
        return redirect('login')

    return render(request, 'store/signup.html')

# ---------------- LOGOUT ----------------
def logout_page(request):
    logout(request)
    messages.success(request, "Logged out successfully")
    return redirect('login')


# ---------------- CART ----------------
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
            'category': category,
            'image': str(product.image) if product.image else None
        }
        request.session['cart'].append(cart_item)
        request.session.modified = True
        messages.success(request, f'{product.name} added to cart!')
    except Product.DoesNotExist:
        messages.error(request, 'Product not found.')

    return redirect('cart')


def remove_from_cart(request, item_id):
    if 'cart' in request.session:
        request.session['cart'] = [
            item for item in request.session['cart']
            if item['id'] != item_id
        ]
        request.session.modified = True

    return redirect('cart')


def cart_page(request):
    cart = request.session.get('cart', [])
    total = sum(item['price'] * item['qty'] for item in cart)
    return render(request, 'store/cart.html', {'cart': cart, 'total': total})


# ---------------- CHECKOUT ----------------
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

            messages.success(
                request,
                f'Thank you {full_name}! Order #{order.id} placed successfully.'
            )

            request.session['cart'] = []
            request.session.modified = True

            return redirect('shop')

        else:
            messages.error(request, 'Please fill in all fields.')

    total = sum(item['price'] * item['qty'] for item in cart)
    return render(request, 'store/checkout.html', {'cart': cart, 'total': total})