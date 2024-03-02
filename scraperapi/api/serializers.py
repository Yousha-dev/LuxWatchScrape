from rest_framework import serializers
from api.models import Product
# ,Image


#create serializers here
class ProductSerializer(serializers.HyperlinkedModelSerializer):
    ref_no=serializers.ReadOnlyField()
    class Meta:
        model=Product
        fields="__all__"
        
        
        
# class ImageSerializer(serializers.HyperlinkedModelSerializer):
#     id=serializers.ReadOnlyField()    
#     class Meta:
#         model=Image
#         fields="__all__"