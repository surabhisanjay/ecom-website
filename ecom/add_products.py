import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecom.settings')
django.setup()

from store.models import Product

# Add women's products
products = [
    {
        "name": "Olive Green Satin Dress",
        "description": "Classic Satin dinner party dress",
        "price": 59.99,
        "category": "women",
        "image": "products/women_1_7CPfzZ3.jpg"
    },
    {
        "name": "Long Sleeved Blazer",
        "description": "Linen Blend for Daily wear",
        "price": 79.99,
        "category": "women",
        "image": "products/women_7_tbFayFV.jpg"
    },
    {
        "name": "Ivory Lunch Dress",
        "description": "Paisley pattern made of Linen cotton blend",
        "price": 29.99,
        "category": "women",
        "image": "products/women_3_fOASBNy.jpg"
    },
    {
        "name": "Yellow Tie-up Top",
        "description": "Rayon Blend sleeveless free size top",
        "price": 14.99,
        "category": "women",
        "image": "products/women_9_7lF2TBe.jpg"
    },
    {
        "name": "Casual White Combo",
        "description": "Fitted vest top in ribbed cotton jersey with fitted jumpsuit",
        "price": 49.99,
        "category": "women",
        "image": "products/women_2_m8eodh7.jpg"
    },
    {
        "name": "White cover up",
        "description": "Mesh material tie around cover up",
        "price": 24.99,
        "category": "women",
        "image": "products/women_8_U4IQXpA.jpg"
    },
    {
        "name": "Fur Winter coat",
        "description": "Short length full sleeved green fur coat",
        "price": 79.99,
        "category": "women",
        "image": "products/women_5_hxXYnxZ.jpg"
    },
    {
        "name": "Brown Daily wear combo",
        "description": "Comes with one fitted tank top, linen shorts and mesh cover up",
        "price": 79.99,
        "category": "women",
        "image": "products/women_6_78BI1Td.jpg"
    },
    {
        "name": "Yellow Beach dress",
        "description": "Tie Strap cotton dress",
        "price": 19.99,
        "category": "women",
        "image": "products/women_4_qiEEN4C.jpg"
    },
    # Men's products
    {
        "name": "Corduroy Jacket",
        "description": "Cotton Corduroy blend, Two colour options available",
        "price": 59.99,
        "category": "men",
        "image": "products/men_8_XhY9lOn.jpg"
    },
    {
        "name": "Ivory Shirt",
        "description": "Rayon Blend Ivory shirt with black lining",
        "price": 14.99,
        "category": "men",
        "image": "products/men_3_UrT8umS.jpg"
    },
    {
        "name": "Emerald Green Pullover",
        "description": "Wool and polyester blend sweater",
        "price": 19.99,
        "category": "men",
        "image": "products/men_9_786FzER.jpg"
    },
    {
        "name": "Formal Daily-Wear Combo",
        "description": "Linen Blend combo comes with - Shirt, Trousers and Blazer",
        "price": 75.00,
        "category": "men",
        "image": "products/men_7_KeIjJpU.jpg"
    },
    {
        "name": "Button Down Shirt Pack",
        "description": "combo comes with - 4 Linen shirts",
        "price": 49.99,
        "category": "men",
        "image": "products/men_6_MtbpVev.jpg"
    },
    {
        "name": "Off-White Shirt",
        "description": "Linen Rayon Blend Formal Shirt for Daily Wear",
        "price": 19.99,
        "category": "men",
        "image": "products/men_5_ZLJiY1b.jpg"
    },
    {
        "name": "Khaki Jacket",
        "description": "Tan self design open front jacket",
        "price": 55.00,
        "category": "men",
        "image": "products/men_4_xQzieGk.jpg"
    },
    {
        "name": "Short Sleeved Shirt",
        "description": "Silk Cottom blend red Shirt",
        "price": 29.99,
        "category": "men",
        "image": "products/men_2_cP2ocED.jpg"
    },
    {
        "name": "Collared Jacket",
        "description": "Jacket in a cotton weave with a collar",
        "price": 49.99,
        "category": "men",
        "image": "products/men_1_BLffj8r.jpg"
    }
]

print("Adding women's products...")
for product_data in products:
    product, created = Product.objects.get_or_create(**product_data)
    status = "✓ Created" if created else "• Already exists"
    print(f"{status}: {product.name} - ${product.price}")

print("\nVerifying products...")
women_products = Product.objects.filter(category="women")
men_products = Product.objects.filter(category="men")
print(f"Total women's products: {women_products.count()}")
print(f"Total men's products: {men_products.count()}")

print("\nDone!")
