from rest_framework import viewsets
from .models import OrderItem
from .serializers import OrderSerializer, OrderListSerializer
from django_filters.rest_framework import DjangoFilterBackend,  FilterSet, CharFilter


class CustomOrderItemFilter(FilterSet):
    products = CharFilter(field_name='product__name', method='filter_products')
    customer = CharFilter(field_name='order__customer__name')

    class Meta:
        model = OrderItem
        fields = ['products', 'customer']

    def filter_products(self, queryset, name, value):
        product_names = value.split(',')
        return queryset.filter(product__name__in=product_names)


class OrderViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = CustomOrderItemFilter
    http_method_names = ['get', 'post', 'put']

    def get_serializer_class(self):
        if self.action == 'list':
            return OrderListSerializer
        return OrderSerializer
