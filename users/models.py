from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Custom simple User model
class User(models.Model):
    class Roles(models.TextChoices):
        CUSTOMER = "CUSTOMER", "Customer"
        PHARMACY = "PHARMACY", "Pharmacy"

    username = models.CharField(max_length=150, unique=True)   # renamed from 'user' → 'username'
    role = models.CharField(max_length=20, choices=Roles.choices, default=Roles.CUSTOMER)

    def is_customer(self):
        return self.role == self.Roles.CUSTOMER
    
    def is_pharmacy(self):
        return self.role == self.Roles.PHARMACY
    
    def __str__(self):
        return self.username   # now works correctly


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    address = models.TextField(max_length=255, null=True, blank=True, default="Not Provided")
    profile_image = models.ImageField(upload_to='profile_images/', null=True, blank=True)

    def __str__(self):
        return self.user.username


class PharmacyDetails(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length =200 , blank=False, null=False)
    address = models.CharField(max_length = 300, blank = False, null = False)
    phone = models.CharField(max_length = 20 , blank = True, null = True)
    email = models.EmailField()
    opening_hours = models.TextField(help_text="e.g., Mon-Fri: 9am-9pm, Sat: 10am-6pm")
   # location = models.PointField()
    latitude = models.FloatField(null = True, blank = True)
    longitude = models.FloatField(null = True, blank = True)
    profile_image = models.ImageField(upload_to='profile_images/', null=True, blank=True)
    license_number = models.CharField(max_length=50, unique=True)

    def save(self, *args, **kwargs):
        if self.location:
            self.latitude = self.location.y
            self.longitude = self.location.x
            super().save(*args, **kwargs)

    def __str__(self):
        return self.name


    def __str__(self):
        return self.user.username
