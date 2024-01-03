from django.db import models

class Product(models.Model):
    product_name=models.CharField(max_length=30,default='')
    category_name=models.CharField(max_length=30,default='')
    description=models.CharField(max_length=100,default='')
    buying_price=models.IntegerField()
    selling_price=models.IntegerField()
    purchase=models.IntegerField()
    sale=models.IntegerField()
    stock =models.IntegerField()
