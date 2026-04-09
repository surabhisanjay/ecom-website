# Django E-Commerce Storefront - Developer Guide

## Adding Products to Men's and Women's Pages

Quick reference guide with sample code for adding products to the e-commerce application.

---

## Quick Start: Using add_products.py Script

### Prerequisites

First, set up the database:

```bash
cd ecom

# Step 1: Create migrations
python manage.py makemigrations

# Step 2: Apply migrations (creates database tables)
python manage.py migrate
```

### Run the Product Script

```bash
# Step 3: Add 3 women's products automatically
python add_products.py
```

### View Products

```bash
# Start server
python manage.py runserver

# Visit: http://127.0.0.1:8000/women/
```

The 3 women's products will be displayed with images!

---

## What add_products.py Does

The `add_products.py` script automatically creates 3 women's products:

| Product | Price | Image |
|---------|-------|-------|
| Summer Dress | $45.99 | summer_dress.jpeg |
| Denim Jacket | $79.99 | denim_jacket.jpeg |
| Casual Blouse | $39.99 | casual_blouse.jpeg |

**Features:**
- ✅ Safe to run multiple times (no duplicates)
- ✅ Uses images from `/media/products/`
- ✅ Shows status in terminal
- ✅ Verifies products were created

---

## Sample Code: Using Django Shell

### Enter Django Shell

```bash
cd ecom
python manage.py shell
```

### Import Product Model

```python
from store.models import Product
```

### Add Women's Products

```python
# Women's product example 1
Product.objects.create(
    name="Summer Dress",
    description="Light and breezy summer dress",
    price=45.99,
    category="women"
)

# Women's product example 2
Product.objects.create(
    name="Denim Jacket",
    description="Classic denim jacket",
    price=79.99,
    category="women"
)

# Women's product example 3
Product.objects.create(
    name="Casual Blouse",
    description="Comfortable everyday blouse",
    price=39.99,
    category="women"
)
```

### Add Men's Products

```python
# Men's product example 1
Product.objects.create(
    name="Polo Shirt",
    description="Classic polo shirt",
    price=34.99,
    category="men"
)

# Men's product example 2
Product.objects.create(
    name="Canvas Jacket",
    description="Durable canvas jacket",
    price=89.99,
    category="men"
)

# Men's product example 3
Product.objects.create(
    name="Chino Pants",
    description="Comfortable chino pants",
    price=54.99,
    category="men"
)
```

### View All Products

```python
# Display all products
products = Product.objects.all()
for product in products:
    print(f"{product.name} - ${product.price} ({product.category})")

# Filter by category
women_products = Product.objects.filter(category="women")
men_products = Product.objects.filter(category="men")

# Count products
total_count = Product.objects.count()
print(f"Total products: {total_count}")
```

### Add Product with Image

```python
from django.core.files.base import ContentFile
from pathlib import Path

# Create product
product = Product.objects.create(
    name="Summer Dress",
    description="Light and breezy summer dress",
    price=45.99,
    category="women"
)

# Add image from file
with open('path/to/image.jpeg', 'rb') as f:
    product.image.save('summer_dress.jpeg', ContentFile(f.read()), save=True)

# Or assign image path (file must exist in media/products/)
product.image = 'products/summer_dress.jpeg'
product.save()
```

### Image Upload Examples

```python
# Example 1: Add women's product with image
Product.objects.create(
    name="Denim Jacket",
    description="Classic denim jacket",
    price=79.99,
    category="women",
    image="products/denim_jacket.jpeg"
)

# Example 2: Add men's product with image
Product.objects.create(
    name="Polo Shirt",
    description="Classic polo shirt",
    price=34.99,
    category="men",
    image="products/polo_shirt.jpeg"
)

# Example 3: Add casual blouse with image
Product.objects.create(
    name="Casual Blouse",
    description="Comfortable everyday blouse",
    price=39.99,
    category="women",
    image="products/casual_blouse.jpeg"
)
```

### Upload Images to Media Directory

```python
# Check if image exists
import os
from pathlib import Path

image_path = Path("media/products/summer_dress.jpeg")
print(f"Image exists: {image_path.exists()}")

# List all product images
product_images = Path("media/products/").glob("*.jpeg")
for img in product_images:
    print(img.name)
```

### Update a Product

```python
# Find and update product
product = Product.objects.get(name="Summer Dress")
product.price = 49.99
product.description = "Updated: Beautiful summer dress"
product.save()
```

### Delete a Product

```python
# Delete by name
Product.objects.filter(name="Summer Dress").delete()

# Delete by ID
Product.objects.filter(id=1).delete()

# Delete all products (use with caution!)
Product.objects.all().delete()
```

### Exit Django Shell

```python
exit()
```

---

## Sample Code: Using Django Admin

### Access Admin Panel

```bash
# Start server
python manage.py runserver

# Navigate to: http://127.0.0.1:8000/admin/
# Login with superuser credentials
```

### Create Superuser (if needed)

```bash
python manage.py createsuperuser
```

---

## Product Model Fields

```python
class Product(models.Model):
    name = models.CharField(max_length=200)                    # Max 200 characters
    description = models.TextField()                            # Unlimited text
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Format: 99999.99
    category = models.CharField(max_length=10)                 # "women" or "men"
    image = models.ImageField(upload_to='products/')           # Optional image file
    created_at = models.DateTimeField(auto_now_add=True)       # Auto-set on creation
    updated_at = models.DateTimeField(auto_now=True)           # Auto-updated on save
```

---

## Quick Reference: Category Values

| Category | Value |
|----------|-------|
| Women's | "women" |
| Men's | "men" |

**Important:** Use exact lowercase values, no spaces.

---

## Examples Application

### Complete Script to Add Sample Products

```python
from store.models import Product

# Clear existing products (optional)
Product.objects.all().delete()

# Women's products
women_products = [
    {"name": "Summer Dress", "desc": "Light and breezy summer dress", "price": 45.99},
    {"name": "Denim Jacket", "desc": "Classic denim jacket", "price": 79.99},
    {"name": "Casual Blouse", "desc": "Comfortable everyday blouse", "price": 39.99},
]

for product in women_products:
    Product.objects.create(
        name=product["name"],
        description=product["desc"],
        price=product["price"],
        category="women"
    )

# Men's products
men_products = [
    {"name": "Polo Shirt", "desc": "Classic polo shirt", "price": 34.99},
    {"name": "Canvas Jacket", "desc": "Durable canvas jacket", "price": 89.99},
    {"name": "Chino Pants", "desc": "Comfortable chino pants", "price": 54.99},
]

for product in men_products:
    Product.objects.create(
        name=product["name"],
        description=product["desc"],
        price=product["price"],
        category="men"
    )

print("Sample products added successfully!")
```

---

## View Products on Website

After adding products, they appear at:

- Women's: `http://127.0.0.1:8000/women/`
- Men's: `http://127.0.0.1:8000/men/`

---

## Image Directory Structure

```
ecomproj/
├── ecom/
│   ├── media/
│   │   └── products/           # Product image location
│   │       ├── summer_dress.jpeg
│   │       ├── denim_jacket.jpeg
│   │       ├── polo_shirt.jpeg
│   │       └── casual_blouse.jpeg
│   ├── static/
│   │   └── images/
│   │       ├── loginpage.jpeg
│   │       └── products/
│   ├── db.sqlite3
│   └── ...
```

### Place Images Here

**For user-uploaded product images:**
```
ecomproj/ecom/media/products/
```

**For static images (login background, etc.):**
```
ecomproj/ecom/static/images/
```

### Image Path Reference in Code

```python
# When adding image, use this format:
image = 'products/summer_dress.jpeg'

# Full path becomes:
# http://127.0.0.1:8000/media/products/summer_dress.jpeg

# Image displays as:
# <img src="/media/products/summer_dress.jpeg">
```

### Accessing Images in Browser

```
# Access product images at:
http://127.0.0.1:8000/media/products/summer_dress.jpeg
http://127.0.0.1:8000/media/products/denim_jacket.jpeg
http://127.0.0.1:8000/media/products/polo_shirt.jpeg

# Access static login image at:
http://127.0.0.1:8000/static/images/loginpage.jpeg
```

### Image URL in HTML Templates

```html
<!-- In template, display product image -->
{% if item.image %}
    <img src="/media/{{ item.image }}" alt="{{ item.name }}" class="product-image">
{% endif %}

<!-- Example with actual path -->
<img src="/media/products/summer_dress.jpeg" alt="Summer Dress" class="product-image">
```

