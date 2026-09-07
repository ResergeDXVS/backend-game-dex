from rest_framework import serializers
from .models import Accounts,Address,CreditCard
from django.contrib.auth.models import User
class UsersSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

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

    def create(self, validated_data):
        password = validated_data.pop("password")
        email = validated_data["email"]

        # Crear el User estándar
        user = User.objects.create_user(
            username=email,  # 👈 importante para que authenticate funcione
            email=email,
            password=password
        )

        # Crear el perfil Accounts asociado
        account = Accounts.objects.create(user=user, **validated_data)
        return account


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = [
            "id",
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
            "id",
            "card_number",
            "expiration",
            "cvc"
        ]

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep.pop("expiration", None)
        rep.pop("cvc", None)
        return rep