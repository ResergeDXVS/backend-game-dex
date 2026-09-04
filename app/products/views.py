from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Products, Companies
from .serializers import ProductSerializers,CompaniesSerializers

CATEGORY_LIST = ["consoles","games","controls","passes","accessories"]

#API para visualizar la información de los productos a detalle
class GetProductDetail(APIView):
    def get(self,request, pk):
        product = Products.objects.filter(pk=pk).first()
        if product:
            company = Companies.objects.filter(pk=product.company_id.id).first()
            serializer = ProductSerializers(product)
            serializer.data['company'] = company.name
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#API para traer 10 productos random para la pantalla principal
class GetProductListMainPage(APIView):
    def get(self,request):
        print("fsdf")
        products = Products.objects.order_by("?")[:10]
        serializer = ProductSerializers(products, many=True)
        return Response(serializer.data)

#API para traer productos por categoria
class GetProductList(APIView):
    def get(self,request,category):
        print(category)
        products = Products.objects.filter(category=category.lower()).order_by("name")
        serializer = ProductSerializers(products, many=True)
        return Response(serializer.data)

#API para ver compañias
class GetCompanies(APIView):
    def get(self,request):
        companies = Companies.objects.all()
        serializer = CompaniesSerializers(companies, many=True)
        return Response(serializer.data)
