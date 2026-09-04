from rest_framework import serializers
from .models import Products, Companies
class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = [
            "id",
            "name",
            "image_url",
            "release_date",
            "description",
            "price",
            "promotion",
            "category",
        ]
        read_only_fields = [
            "id",
            "name",
            "image_url",
            "release_date",
            "description",
            "price",
            "promotion",
            "category",
        ]

class CompaniesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Companies
        fields = [
            "id",
            "name",
            "image_url",
        ]
        read_only_fields = [
            "id",
            "name",
            "image_url",
        ]