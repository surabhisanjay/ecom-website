from django.contrib import admin
from .models import Product, Order, OrderItem, CartItem


# =========================
# PRODUCT ADMIN
# =========================
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'created_at')
    list_filter = ('category', 'created_at')
    search_fields = ('name', 'description')
    ordering = ('-created_at',)


# =========================
# ORDER ITEM INLINE (inside Order)
# =========================
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ('price', 'get_total')


# =========================
# ORDER ADMIN
# =========================
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'email', 'total_amount', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('full_name', 'email', 'phone')
    readonly_fields = ('created_at', 'updated_at')
    inlines = [OrderItemInline]
    ordering = ('-created_at',)


# =========================
# ORDER ITEM ADMIN
# =========================
@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'product', 'quantity', 'price', 'get_total')
    readonly_fields = ('get_total',)


# =========================
# CART ITEM ADMIN (NEW 🔥)
# =========================
@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'product', 'quantity')
    search_fields = ('user__username', 'product__name')