from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from .models import Accounts, Address, CreditCard
from .serializers import UsersSerializer, AddressSerializer, CreditCardSerializer

class APILogin(APIView):
    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")
        print(request.data)
        try:
            user = Accounts.objects.get(email=email)
        except Accounts.DoesNotExist:
            return Response({"error": "Usuario no encontrado"}, status=status.HTTP_404_NOT_FOUND)

        if user.check_password(password):
            refresh = RefreshToken.for_user(user)
            return Response({
                "user": {
                    "id": user.id,
                    "email": user.email,
                    "name": user.name,
                    "paternal_surname": user.paternal_surname,
                    "maternal_surname": user.maternal_surname,
                },
                "access": str(refresh.access_token),
                "refresh": str(refresh)
            }, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Contraseña incorrecta"}, status=status.HTTP_401_UNAUTHORIZED)
        
class APIUser(APIView):
    def post(self, request):
        print(request.data)
        serializer = UsersSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            return Response({
                "user": {
                    "id": user.id,
                    "email": user.email,
                    "name": user.name,
                    "paternal_surname": user.paternal_surname,
                    "maternal_surname": user.maternal_surname,
                },
                "access": str(refresh.access_token),
                "refresh": str(refresh)
            }, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class APIAddress(APIView):
    permission_classes = [IsAuthenticated]
    def post(self,request):
        serializer = AddressSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(account=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        addresses = Address.objects.filter(account_id=request.user)
        serializer = AddressSerializer(addresses, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class APICreditCard(APIView):
    permission_classes = [IsAuthenticated]
    def post(self,request):
        serializer = AddressSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        addresses = Address.objects.filter(account_id=request.user)
        serializer = CreditCardSerializer(addresses, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)