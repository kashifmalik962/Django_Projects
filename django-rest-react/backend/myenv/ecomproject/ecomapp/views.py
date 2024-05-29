from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
# from .products import Products
from .models import Product
from .serializer import ProductSerializer

# Create your views here.
@api_view(['GET'])
def getRoutes(request):
    return Response("Hello, world! This is the index page.")


@api_view(['GET'])
def getProducts(request):
    products=Product.objects.all()
    serializer=ProductSerializer(products,many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getProduct(request,pk):
    products=Product.objects.get(_id=pk)
    serializer=ProductSerializer(products,many=False)
    return Response(serializer.data)