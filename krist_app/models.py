
from django.db import models


class userAccount(models.Model):
    Name = models.CharField(max_length=200)
    Email = models.EmailField(max_length=200)
    Password = models.CharField(max_length=100)
    
    is_created = models.DateTimeField(auto_now_add=True)
    
    
class products(models.Model):
    product_id = models.IntegerField(primary_key=True)
    productname = models.CharField(max_length=100)
    productcategory = models.CharField(max_length=50)
    productprice = models.DecimalField(max_digits=10,decimal_places=2,null=False,blank=False)
    productdescription = models.CharField(max_length=200)
    productimage = models.ImageField(upload_to="product/image")

class UserOtp(models.Model):
    Email = models.CharField(max_length=100)
    otp = models.IntegerField()
    
    
class cart(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    image = models.ImageField(blank=True)
    
class order(models.Model):
    order_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=100)
    user_address = models.CharField(max_length=200)
    user_moblieno = models.CharField(max_length=50)
    product_name = models.CharField(max_length=100)
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    product_qty = models.IntegerField()

class admin(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    
    

    
   
   
    