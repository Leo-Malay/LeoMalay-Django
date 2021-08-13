from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=200, unique=True, blank=False)
    p_type = models.CharField(max_length=15)
    price = models.IntegerField()
    content = models.TextField()
    desc = models.TextField()
    image = models.ImageField(upload_to="media/IMG/")
    soldby = models.CharField(max_length=50, blank=False)
    rating = models.FloatField(max_length=5)

    def __str__(self):
        return self.name


"""

class Order(models.Model):
    customer_id = models.IntegerField()
    payable_amount = models.FloatField()

    def __str__(self):
        return
"""
