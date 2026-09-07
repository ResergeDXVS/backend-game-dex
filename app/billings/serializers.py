from rest_framework import serializers
from .models import Billing
from accounts.serializers import AddressSerializer, CreditCardSerializer
from orders.models import Orders
from orders.serializers import OrdersSerializer

class BillingSerializer(serializers.ModelSerializer):
    address = AddressSerializer(source="address_id", read_only=True)
    payment = CreditCardSerializer(source="payment_id", read_only=True)
    orders = OrdersSerializer(many=True, read_only=True)

    class Meta:
        model = Billing
        fields = [
            "id",
            "account_id",
            "address_id",
            "payment_id",
            "total",
            "address",
            "payment",
            "orders"
        ]


    def create(self, validated_data):
        orders_data = validated_data.pop("orders", [])
        billing = Billing.objects.create(**validated_data)

        print(billing.id)
        for order_data in orders_data:
            Orders.objects.create(billing=billing, **order_data)
        return billing