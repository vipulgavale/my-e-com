from django.db import models

# Create your models here.
class Product(models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    sub_category=models.CharField(max_length=100)
    price=models.IntegerField(default=0)
    product_descpt=models.CharField(max_length=500)
    creation_date=models.DateField()
    image=models.ImageField(upload_to='shop/image')

    def __str__(self):
        return self.product_name
    