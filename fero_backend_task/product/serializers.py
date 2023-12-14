from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def validate_name(self, value):
        if Product.objects.filter(name=value).exists():
            raise serializers.ValidationError("This product name is already in use. Please choose a different name.")
        return value

    def validate_weight(self, value):
        if 0 < value <= 25:
            return value
        raise serializers.ValidationError("Product must be greater than 0 and not exceed 25 kg.")
