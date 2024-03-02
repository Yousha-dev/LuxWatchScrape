from django.contrib import admin
from api.models import Product
#,Image
# Register your models here..

class ProductAdmin(admin.ModelAdmin):
    list_display=('ref_no','brand','model','price','source')
    search_fields=('brand',)   
    
# class ImageAdmin(admin.ModelAdmin):
#     list_display=('product','location')
#     list_filter=('product',)

admin.site.register(Product,ProductAdmin)
# admin.site.register(Image,ImageAdmin)

