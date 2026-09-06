from rest_framework import serializers
from .models import Accounts,Address,CreditCard
class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accounts
        fields = [
            "id",
            "name",
            "paternal_surname",
            "maternal_surname",
            "rfc",
            "datebirth",
            "email",
            "password",
        ]


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = [
            "id",
            "account_id",
            "address",
            "internal_number",
            "external_number",
            "postal",
            "suburb",
            "country"
        ]

class CreditCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreditCard
        fields = [
            "account_id",
            "card_number",
            "expiration",
            "cvc"
        ]