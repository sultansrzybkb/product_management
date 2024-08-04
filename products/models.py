from django.db import models

# Create your models here.
class Category (models.Model):
 name= models.CharField(max_length=200)

 def __str__(self):
    return self.name
class Product(models.Model):
  name=models.CharField(max_length=200)
  description =models.TextField(blank=True)
  category = models.ForeignKey(Category,on_delete=models.CASCADE)  
  price= models.DecimalField(max_digits=15,decimal_places=2)

  def __str__(self):
    return self.name
