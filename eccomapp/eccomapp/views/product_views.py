from eccomapp.serializer import ProductSerializer, DairyProductSerializer
from rest_framework.views import APIView 
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from eccomapp.models import Product
from eccomapp.models import DiaryProduct


class ListCreateProductAPIView(APIView):
    
    def get(self, request):
        products = Product.objects.all()
        # products = Product.objects.all().filter(price__gt=100) #grater than 100
        # products = Product.objects.all().filter(price=100)
        # products = Product.objects.all().filter(price__in=[100, 200]) # in between 100 to 200 
        # products = Product.objects.raw('SELECT * FROM eccomapp_product WHERE price BETWEEN 60.0 AND 100.0')
        # products = Product.objects.raw('SELECT * FROM eccomapp_product')
        serialized = ProductSerializer(products, many=True)
        return Response(serialized.data , status=200)
        # return Response(serialized.data , status=200)
        # return Response({"products": products})
    
    def post(self, request):
        data = request.data
        decoded_data = ProductSerializer(data=data)
        if not decoded_data.is_valid():
            return  Response(decoded_data.errors, status=400)
        
        decoded_data.save()
        return  Response(decoded_data.data, status=200)
        
class DairyListCreateAPIView(ListCreateAPIView):
    queryset = DiaryProduct.objects.all()
    serializer_class = DairyProductSerializer

class DairyRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = DiaryProduct.objects.all()
    serializer_class = DairyProductSerializer