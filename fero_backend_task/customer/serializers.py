from rest_framework import serializers
from .models import Customer


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

    @staticmethod
    def validate_name(value):
        # Check if the name is unique
        if Customer.objects.filter(name=value).exists():
            raise serializers.ValidationError("This customer name is already in use. Please choose a different name.")
        return value
