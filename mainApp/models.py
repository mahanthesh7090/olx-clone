from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=50)  # e.g., 'Car', 'Bike', 'Mobile'
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    brand = models.CharField(max_length=20)
    year = models.IntegerField()
    noOfOwner = models.IntegerField()
    location = models.CharField(max_length=20)
    address = models.TextField()
    phno = models.CharField(max_length=20)

    class Meta:
        abstract = True  

class Cars(Product):
    fuel = models.CharField(max_length=50)
    transmission = models.CharField(max_length=50)
    km = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='images/cars/', blank=True, null=True)
    image1 = models.ImageField(upload_to='images/cars/', blank=True, null=True)
    image2 = models.ImageField(upload_to='images/cars/', blank=True, null=True)
    image3 = models.ImageField(upload_to='images/cars/', blank=True, null=True)
    seller = models.ForeignKey(User, related_name='car_products', on_delete=models.CASCADE)

class Bikes(Product):
    bikeKm = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='images/bikes/', blank=True, null=True)
    image1 = models.ImageField(upload_to='images/bikes/', blank=True, null=True)
    image2 = models.ImageField(upload_to='images/bikes/', blank=True, null=True)
    image3 = models.ImageField(upload_to='images/bikes/', blank=True, null=True)
    seller = models.ForeignKey(User, related_name='bike_products', on_delete=models.CASCADE)


class Mobiles(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=50)  # e.g., 'Car', 'Bike', 'Mobile'
    seller = models.ForeignKey(User, related_name='mobiles_products', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    brand = models.CharField(max_length=20)
    image = models.ImageField(upload_to='images/mobiles/', blank=True, null=True)
    image1 = models.ImageField(upload_to='images/mobiles/', blank=True, null=True)
    image2 = models.ImageField(upload_to='images/mobiles/', blank=True, null=True)
    image3 = models.ImageField(upload_to='images/mobiles/', blank=True, null=True)
    location = models.CharField(max_length=20)
    address = models.TextField()
    phno = models.CharField(max_length=20)

class Applications(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=50)  # e.g., 'Car', 'Bike', 'Mobile'
    seller = models.ForeignKey(User, related_name='application_products', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/applications/', blank=True, null=True)
    image1 = models.ImageField(upload_to='images/applications/', blank=True, null=True)
    image2 = models.ImageField(upload_to='images/applications/', blank=True, null=True)
    image3 = models.ImageField(upload_to='images/applications/', blank=True, null=True)
    location = models.CharField(max_length=20)
    address = models.TextField()
    phno = models.CharField(max_length=20)
