from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate
from .models import Accounts, Address, CreditCard
from .serializers import UsersSerializer, AddressSerializer, CreditCardSerializer

class APILogin(APIView):
    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")

        # Autenticar contra el modelo User
        user = authenticate(username=email, password=password)
        if user is None:
            return Response({"error": "Usuario o contraseña incorrectos"}, status=status.HTTP_401_UNAUTHORIZED)

        # Obtener el perfil Accounts asociado
        try:
            account = Accounts.objects.get(user=user)
        except Accounts.DoesNotExist:
            return Response({"error": "Perfil no encontrado"}, status=status.HTTP_404_NOT_FOUND)

        # Generar tokens JWT
        refresh = RefreshToken.for_user(user)
        return Response({
            "user": {
                "id": user.id,
                "email": user.email,
                "name": account.name,
                "paternal_surname": account.paternal_surname,
                "maternal_surname": account.maternal_surname,
                "rfc": account.rfc,
                "datebirth": account.datebirth,
            },
            "access": str(refresh.access_token),
            "refresh": str(refresh)
        }, status=status.HTTP_200_OK)
        
class APIUser(APIView):
    def post(self, request):
        serializer = UsersSerializer(data=request.data)
        if serializer.is_valid():
            # El serializer crea User + Accounts
            account = serializer.save()

            # Generar tokens JWT a partir del User
            refresh = RefreshToken.for_user(account.user)

            return Response({
                "user": {
                    "id": account.user.id,
                    "email": account.user.email,
                    "name": account.name,
                    "paternal_surname": account.paternal_surname,
                    "maternal_surname": account.maternal_surname,
                    "rfc": account.rfc,
                    "datebirth": account.datebirth,
                },
                "access": str(refresh.access_token),
                "refresh": str(refresh)
            }, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class APIAddress(APIView):
    permission_classes = [IsAuthenticated]
    def post(self,request):
        serializer = AddressSerializer(data=request.data)
        print(serializer)
        print(request.data)
        if serializer.is_valid():
            account = Accounts.objects.get(email=request.user.email)
            serializer.save(account_id=account)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        account = Accounts.objects.get(email=request.user.email)
        addresses = Address.objects.filter(account_id=account)
        serializer = AddressSerializer(addresses, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class APICreditCard(APIView):
    permission_classes = [IsAuthenticated]
    def post(self,request):
        serializer = CreditCardSerializer(data=request.data)
        if serializer.is_valid():
            account = Accounts.objects.get(email=request.user.email)
            serializer.save(account_id=account)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        account = Accounts.objects.get(email=request.user.email)
        cards = CreditCard.objects.filter(account_id=account)
        serializer = CreditCardSerializer(cards, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)