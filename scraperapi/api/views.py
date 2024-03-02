from django.shortcuts import render
from rest_framework import viewsets
from api.models import Product
# ,Image
from api.serializers import ProductSerializer
#,ImageSerializer
from rest_framework.decorators import action
# Create your views here.
class ProductViewSet(viewsets.ModelViewSet):
    queryset= Product.objects.all()
    serializer_class=ProductSerializer
    lookup_value_regex = '[^/]+' #to allow special characters in url
    #products/{productId}/images
#     @action(detail=True,methods=['get'])
#     def images(self,request,pk=None):   
#         try:                
#             product=Product.objects.get(pk=pk)
#             emps=Image.objects.filter(product=product)
#             emps_serializer=ImageSerializer(emps,many=True,context={'request':request})
#             return Response(emps_serializer.data)
#         except Exception as e:
#             print(e)
#             return Response({
#                 'message':'Product does not exists or has no images'
#             })


# class ImageViewSet(viewsets.ModelViewSet):
#     queryset=Image.objects.all()
#     serializer_class=ImageSerializer