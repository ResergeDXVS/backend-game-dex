from rest_framework import serializers
from .models import Orders
from products.serializers import ProductSerializers
class OrdersSerializer(serializers.ModelSerializer):
    product = ProductSerializers(read_only=True)

    class Meta:
        model = Orders
        fields = ["id", "product", "count", "total"]