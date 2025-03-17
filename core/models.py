from django.db import models

# Create your models here.
class AmazoneDataScrape(models.Model):
    product_name = models.TextField(max_length=100)
    product_price = models.TextField(max_length=100)
    product_time = models.TextField(max_length=100)
    product_image = models.ImageField(upload_to='pictures')
    
    def __str__(self):
        return self.product_name
    
    
    