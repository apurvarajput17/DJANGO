from django.db import models

# Create your models here.
class Customer(models.Model):
    cid = models.IntegerField(primary_key=True)
    cnm = models.CharField(max_length=34)
    product = models.CharField(max_length=23)
    quantity = models.IntegerField()
    price = models.IntegerField()
