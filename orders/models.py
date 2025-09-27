from django.db import models
from django.conf import settings

# Create your models here.
class Order(models.Model):
    class Order_Type(models.TextChoices):
        DELIVERY = 'DELIVERY', 'Delivery'
        Reservation = 'RESERVATION', 'Reservation'

    class Order_Status(models.TextChoices):
        PENDING = 'PENDING', 'Pending'
        PROCESSING = 'PROCESSING', 'Processing'
        OUT_FOR_DELIVERY = 'OUT_FOR_DELIVERY', 'Out_For_Delivery'
        COMPLETED = 'COMPLETED', 'Completed'
        CANCELLED = 'CANCELLED', 'Cancelled'

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    pharmacy = models.ForeignKey('pharmacies.PharmacyDetails', on_delete=models.CASCADE)
    order_type = models.CharField(max_length=20, choices=Order_Type.choices)
    order_status = models.CharField(max_length=20, choices=Order_Status.choices, default=Order_Status.PENDING)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    delivery_address = models.CharField(max_length=300, blank=True, null=True)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    medicine_name = models.ForeignKey('catalog.MedicineDetails', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price_at_purchase = models.DecimalField(max_digits=10, decimal_places=2)

class Payment(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    transaction_id = models.CharField(max_length=100, unique=True)
    payment_status = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)


      
