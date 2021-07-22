from django.db import models

# Create your models here.



class catergory(models.Model):
    cat_name = models.CharField(max_length=50)
    cat_image = models.ImageField(null=True,upload_to= 'images/')

    def __str__(self):
        return self.cat_name
    
class product(models.Model):
    product_name = models.CharField(max_length=100)
    product_price =models.PositiveIntegerField(default=45000)
    product_cat = models.ForeignKey(catergory,on_delete=models.CASCADE)
    product_image = models.ImageField(null=True,upload_to='images/')
    product_dis =models.TextField

    def __str__(self):
        return self.product_name
    
