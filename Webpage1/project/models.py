from django.conf import settings
from django.db import models

class Category(models.Model):
  category = models.CharField(max_length=50,null =True)
  subcateg = models.CharField(max_length=50,null = True)
  product = models.CharField(max_length=50,null = True)
   

   
  


