from django.db import models

from customer.models import Customer
from product.models import Product


class Order(models.Model):
    order_number = models.CharField(max_length=10, unique=True, editable=False)
    customer = models.ForeignKey(Customer, related_name='customer_orders', on_delete=models.CASCADE)
    order_date = models.DateField()
    address = models.CharField(max_length=255)

    def save(self, *args, **kwargs):
        # Generate order_number with prefix ORD and a sequential number
        if not self.order_number:
            last_order = Order.objects.order_by('-id').first()
            if last_order:
                last_number = int(last_order.order_number[3:])
                self.order_number = f'ORD{str(last_number + 1).zfill(5)}'
            else:
                self.order_number = 'ORD00001'
        super(Order, self).save(*args, **kwargs)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='order_items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_products', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
