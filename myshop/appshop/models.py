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
    description = models.CharField(max_length=200)
    price = models.FloatField()
    is_enabled = models.BooleanField()
    small_photo = models.ImageField()
    big_photo = models.ImageField()
    is_featured = models.BooleanField()
    is_really_hot = models.BooleanField()
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






