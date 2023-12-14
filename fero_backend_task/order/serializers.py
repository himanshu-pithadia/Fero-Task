from rest_framework import serializers
from .models import Order, OrderItem
from datetime import datetime
from product.models import Product

from product.serializers import ProductSerializer

from customer.serializers import CustomerSerializer


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['order', 'product', 'quantity']


class OrderSerializer(serializers.ModelSerializer):
    order_item = serializers.ListField(child=serializers.DictField(), write_only=True)

    class Meta:
        model = Order
        fields = ['customer', 'order_date', 'address', 'order_item']

    def to_internal_value(self, data):
        data['order_date'] = datetime.strptime(data['order_date'], "%d/%m/%Y").date()
        return super(OrderSerializer, self).to_internal_value(data)

    def validate(self, data):
        order_items_data = data.get('order_item', [])
        total_weight = 0

        for item_data in order_items_data:
            product_id = item_data['product']
            quantity = item_data['quantity']

            # Fetch the product instance
            try:
                product_instance = Product.objects.get(pk=product_id)
            except Product.DoesNotExist:
                raise serializers.ValidationError(f"Product does not exist.")

            # Calculate and accumulate the weight for valid products
            total_weight += product_instance.weight * quantity

        if total_weight > 150:
            raise serializers.ValidationError("Order cumulative weight must be under 150kg.")

        return data

    def create(self, validated_data):
        order_items_data = validated_data.pop('order_item')
        order = Order.objects.create(**validated_data)

        for item_data in order_items_data:
            product_id = item_data['product']
            quantity = item_data['quantity']
            # OrderItem.objects.create(order=order, **item_data)
            OrderItem.objects.create(order=order, product_id=product_id, quantity=quantity)
        return order


class OrderListSerializer(serializers.ModelSerializer):
    order_id = serializers.IntegerField(source='order.id', read_only=True)
    order_number = serializers.CharField(source='order.order_number', read_only=True)
    customer = serializers.SerializerMethodField()
    order_date = serializers.DateField(source='order.order_date', read_only=True)
    address = serializers.CharField(source='order.address', read_only=True)
    product = serializers.CharField(source='product.name', read_only=True)

    class Meta:
        model = OrderItem
        fields = ['order_id', 'order_number', 'customer', 'order_date', 'address', 'product', 'quantity']
        # fields = '__all__'

    @staticmethod
    def get_customer(obj):
        return obj.order.customer.name
