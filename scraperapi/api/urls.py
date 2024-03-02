from django.contrib import admin
from django.urls import path,include
from api.views import ProductViewSet
# ,ImageViewSet
from rest_framework import routers


router= routers.DefaultRouter()
router.register(r'products', ProductViewSet)
# router.register(r'images', ImageViewSet)

urlpatterns = [    
    path('',include(router.urls))
      
]


#products/{productId}/images