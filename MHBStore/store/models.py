from django.db import models


class Promotion (models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    discount = models.FloatField()


class Category (models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    creted_at = models.DateTimeField(auto_created=True)
    featured_product = models.ForeignKey(
        'Product', on_delete=models.SET_NULL, null=True, related_name='+')
    '''
        * on_delete=models.SET_NULL -> to delete a featured product for the category, set this field to null
        * use 'Product' to resolve conflicts Product name class. the string will not be update later in order to class name changes
        *  related_name='+' -> django will not create the reverse relation ship
    '''


class Product (models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    slug = models.SlugField(default='-', null=True)
    promotions = models.ManyToManyField(Promotion)
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now_add=True)
    creted_at = models.DateTimeField(auto_created=True)


membership_gold = 'G'
membership_silver = 'S'
membership_bronze = 'B'


membership_choices = [
    (membership_gold, 'Gold'),
    (membership_silver, 'Silver'),
    (membership_bronze, 'Bronze')
]


class Customer (models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    phone = models.CharField(max_length=255)
    birth_date = models.DateField(null=True)
    membership = models.CharField(
        max_length=1, choices=membership_choices, default='B')


PAYMENT_STATUS_PENDING = 'P'
PAYMENT_STATUS_SUCCESS = 'S'
PAYMENT_STATUS_FAILED = 'F'

PAYMENT_CHOICES = [
    (PAYMENT_STATUS_PENDING, 'Pending'),
    (PAYMENT_STATUS_SUCCESS, 'Success'),
    (PAYMENT_STATUS_FAILED, 'Failed')
]


class Order(models.Model):
    customer = models.ForeignKey(
        Customer, on_delete=models.PROTECT)
    placed_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(max_length=1,
                                      choices=PAYMENT_CHOICES, default=PAYMENT_STATUS_PENDING)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveSmallIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)


class Address(models.Model):
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE)
    country = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    street1 = models.CharField(max_length=255)
    street2 = models.CharField(max_length=255, null=True)


class Cart (models.Model):
    creted_at = models.DateTimeField(auto_now_add=True)


class CartItem (models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE)  # CASCADE is for delete a product from all shopping carts
    quantity = models.PositiveSmallIntegerField()
