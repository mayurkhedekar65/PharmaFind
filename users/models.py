from django.db import models

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


class Pharmacy(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    address = models.TextField(max_length=255, null=True, blank=True, default="Not Provided")
    profile_image = models.ImageField(upload_to='profile_images/', null=True, blank=True)
    license_number = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.user.username
