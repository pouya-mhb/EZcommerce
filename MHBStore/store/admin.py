from django.contrib import admin
from store.models import Promotion, Category, Product, Customer, Order, OrderItem, Address, Cart, CartItem


@admin.register(Promotion)
class PromotionAdmin(admin.ModelAdmin):
    list_display = ['title', 'discount']
    search_fields = ['title']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'inventory', 'last_update']
    search_fields = ['title']
    list_filter = ['category', 'last_update']

    class Meta:
        # Added Meta class to filter by category and product
        ordering = ['category', 'title']


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'phone', 'membership']
    search_fields = ['first_name', 'last_name', 'email']
    list_filter = ['membership']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer', 'placed_at', 'payment_status']
    list_filter = ['payment_status', 'placed_at']


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'product', 'quantity', 'unit_price']
    list_filter = ['order']


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ['customer', 'country', 'city', 'street1']
    search_fields = ['customer__first_name',
                     'customer__last_name', 'country', 'city']


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ['cart', 'product', 'quantity']
    list_filter = ['cart']
