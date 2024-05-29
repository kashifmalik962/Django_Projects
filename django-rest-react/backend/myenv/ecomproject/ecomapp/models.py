from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    productname=models.CharField(max_length=150)
    image=models.ImageField(null=True,blank=True)
    productbrand=models.CharField(max_length=100,null=True,blank=True)
    brandcategory=models.CharField(max_length=100,null=True,blank=True)
    productinfo=models.TextField(null=True,blank=True)
    rating=models.DecimalField(max_digits=8,decimal_places=2)
    numReviews=models.IntegerField(null=True,blank=True,default=0)
    price=models.CharField(max_length=7,null=True,blank=True)
    stockcount=models.IntegerField(null=True,blank=True,default=True)
    createdAt=models.DateTimeField(auto_now_add=True)
    _id=models.AutoField(primary_key=True,editable=False)
    
    def __str__(self):
        return self.productname