# Django E-Commerce Project Report

## Project Overview
A simple Django-based e-commerce storefront built for selling women's and men's clothing with user authentication, product browsing, and shopping cart functionality.

## Project Structure
```
ecomproj/
├── ecom/                          # Main Django project
│   ├── __init__.py
│   ├── settings.py               # Project configuration
│   ├── urls.py                   # Main URL router
│   ├── asgi.py
│   └── wsgi.py
├── store/                         # Django app
│   ├── migrations/
│   ├── templates/store/
│   │   ├── base.html             # Base template with navigation
│   │   ├── home.html             # Shop homepage
│   │   ├── login.html            # Login page
│   │   ├── womens.html           # Women's clothing catalog
│   │   ├── mens.html             # Men's clothing catalog
│   │   └── cart.html             # Shopping cart page
│   ├── views.py                  # View functions
│   ├── urls.py                   # App URL routing
│   ├── models.py
│   ├── admin.py
│   ├── apps.py
│   └── tests.py
├── manage.py                      # Django management script
├── requirements.txt               # Python dependencies
└── .gitignore
```

## Features Implemented

### 1. **Login Page**
- Landing page for all users
- Beige and pastel color scheme
- Accepts any username and password combination
- Session management for cart persistence
- Redirects to shop after login

### 2. **Women's Clothing Page**
- Displays 3 sample products: Summer Dress, Denim Jacket, Casual Blouse
- Product cards with name, description, and price
- "Add to Cart" functionality
- Responsive grid layout

### 3. **Men's Clothing Page**
- Displays 3 sample products: Polo Shirt, Canvas Jacket, Chino Pants
- Product cards with name, description, and price
- "Add to Cart" functionality
- Responsive grid layout

### 4. **Shopping Cart Page**
- Displays all items added to cart
- Shows item name, price, and remove option
- Calculates and displays total
- Empty cart message with links to shop
- Session-based storage (persists during session)

### 5. **Navigation**
- Header with links to all pages
- Beige/tan color scheme (#e8dcc8)
- Accessible from all pages except login

## Color Scheme
- **Background**: Warm beige (#faf7f2)
- **Header**: Light tan (#e8dcc8)
- **Cards**: Off-white (#fff9f4)
- **Primary Button**: Warm tan (#d4a574)
- **Text**: Brown (#5a4a42)
- **Accents**: Pastel tones

## Technology Stack
- **Framework**: Django 4.2+
- **Database**: SQLite (default)
- **Frontend**: HTML5 + CSS3
- **Backend**: Python
- **Session Management**: Django sessions

## URL Routes
| Route | Name | View | Description |
|-------|------|------|-------------|
| `/` | home | login_page | Landing/login page |
| `/shop/` | shop | home | Shop homepage |
| `/women/` | women | womens_clothing | Women's products |
| `/men/` | men | mens_clothing | Men's products |
| `/login/` | login | login_page | Login page |
| `/cart/` | cart | cart_page | Shopping cart |
| `/add-to-cart/<id>/<category>/` | add_to_cart | add_to_cart | Add item to cart |
| `/remove-from-cart/<id>/` | remove_from_cart | remove_from_cart | Remove item from cart |

## Setup Instructions

### 1. Create Virtual Environment
```bash
cd /Users/chandrikasanjay/ecomproj/ecom
python3 -m venv venv
source venv/bin/activate
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run Migrations
```bash
python manage.py migrate
```

### 4. Start Development Server
```bash
python manage.py runserver
```

### 5. Access the Application
Open browser and navigate to: `http://127.0.0.1:8000/`

## Key Functionality Details

### Login System
- No database validation (all credentials accepted)
- Initializes empty cart session on login
- Success message displays username

### Shopping Cart
- Session-based (not database-backed)
- Items stored with: id, name, price, quantity, category
- Persists during user session
- Cart totals calculated dynamically

### Product Catalog
- Men's items: Polo Shirt ($34.99), Canvas Jacket ($89.99), Chino Pants ($54.99)
- Women's items: Summer Dress ($45.99), Denim Jacket ($79.99), Casual Blouse ($39.99)
- Products stored in Python lists (can be migrated to database)

## Future Enhancements
- User authentication with database
- Product database model
- Order history tracking
- Payment gateway integration
- Product search and filtering
- User profile management
- Admin panel for product management
- Email notifications

## Notes
- All passwords are accepted for demo purposes
- Cart is session-based and not persisted to database
- No user accounts are created (demo mode)
- Database uses SQLite by default

---
**Project Created**: April 7, 2026
**Status**: Fully Functional Demo
