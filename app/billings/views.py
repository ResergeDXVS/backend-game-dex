from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Billing
from .serializers import BillingSerializer, OrdersSerializer

class APIBilling(APIView):
    def post(self, request):
        billing_serializer = BillingSerializer(data=request.data)
        if billing_serializer.is_valid():
            billing = billing_serializer.save()
            return Response(BillingSerializer(billing).data, status=status.HTTP_201_CREATED)
        return Response(billing_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def get(self, request):
        billing = Billing.objects.order_by("-id").first()
        serializer = BillingSerializer(billing)
        return Response(serializer.data, status=status.HTTP_200_OK)