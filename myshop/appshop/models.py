from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=200)
    short_description = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)
    short_description = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    price = models.FloatField()
    slider = models.BooleanField()
    photo = models.ImageField()
    in_stock = models.BooleanField()
    on_main_page = models.BooleanField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Order(models.Model):
    number = models.PositiveSmallIntegerField(default=0)
    unique_code = models.PositiveSmallIntegerField()
    person_name = models.CharField(max_length=200)
    person_email = models.EmailField()
    person_phone = models.CharField(max_length=200)
    notes = models.CharField(max_length=200)

    STATUS_CHOICES = (
        ('New', 'New'),
        ('In process', 'In process'),
        ('Ready to deliver', 'Ready to deliver'),
        ('Delivering', 'Delivering'),
        ('Delivered', 'Delivered'),
        ('Suspended', 'Suspended'),
        ('Cancelled', 'Cancelled')
    )
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='New')
    comment = models.CharField(max_length=200)


class OrderedProduct(models.Model):
    quantity = models.PositiveSmallIntegerField(default=0)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)






