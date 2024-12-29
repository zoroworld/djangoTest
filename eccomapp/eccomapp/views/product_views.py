from rest_framework.views import APIView
from rest_framework.response import Response
from eccomapp.models import Product

class ProductApiView(APIView):
    def get(self, request):
        products = Product.objects.all()
        return Response({"products": products})
