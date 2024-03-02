from django.db import models

# Create your models here.

#Creating Product Model

class Product(models.Model):
    ref_no= models.CharField(max_length=30,primary_key=True)
    brand= models.CharField(max_length=50)
    model= models.CharField(max_length=50)
    price= models.CharField(max_length=15)
    images= models.JSONField()
    source= models.URLField()
    details= models.JSONField()
    
    # specifications=models.TextField()
    # characteristics=models.TextField()
    # origin=models.CharField(max_length=50)
    # gender=models.CharField(max_length=10,choices=
    #                       (('Mens','Mens'),
    #                        ('Ladies','Ladies'),
    #                        ("Unisex",'Unisex')
    #                        ))
    # warranty=models.TextField()
    # warranty_ext=models.TextField()
    # active=models.BooleanField(default=True)
    
#     def __str__(self):
#         return self.brand_name +' - '+ self.product_name
    
    
    
# #Image Model
# class Image(models.Model):
#     product=models.ForeignKey(Product, on_delete=models.CASCADE)
#     location=models.TextField()
    
    
    
    