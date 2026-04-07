import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecom.settings')
django.setup()

from store.models import Product

# Add women's products
products = [
    {
        "name": "Summer Dress",
        "description": "Light and breezy summer dress perfect for warm days",
        "price": 45.99,
        "category": "women",
        "image": "products/summer_dress.jpeg"
    },
    {
        "name": "Denim Jacket",
        "description": "Classic denim jacket for all seasons",
        "price": 79.99,
        "category": "women",
        "image": "products/denim_jacket.jpeg"
    },
    {
        "name": "Casual Blouse",
        "description": "Comfortable everyday blouse",
        "price": 39.99,
        "category": "women",
        "image": "products/casual_blouse.jpeg"
    }
]

print("Adding women's products...")
for product_data in products:
    product, created = Product.objects.get_or_create(**product_data)
    status = "✓ Created" if created else "• Already exists"
    print(f"{status}: {product.name} - ${product.price}")

print("\nVerifying products...")
women_products = Product.objects.filter(category="women")
print(f"Total women's products: {women_products.count()}")

print("\nDone!")
