from rest_framework import viewsets
from .models import Order, OrderItem
from .serializers import OrderSerializer, OrderListSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    http_method_names = ['get', 'post', 'put']

    def get_serializer_class(self):
        if self.action == 'list':
            return OrderListSerializer
        return OrderSerializer
