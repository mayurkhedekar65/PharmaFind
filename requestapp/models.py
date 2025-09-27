from django.db import models
from django.conf import settings
from pharmacies.models import PharmacyDetails
# Create your models here.

class MedicineRequest(models.Model):
    class Status(models.TextChoices):
        PENDING = 'PENDING', 'Pending'
        NOTIFIED = 'NOTIFIED', 'User Notified'
        FULFILLED = 'FULFILLED', 'Request Fulfilled'

    user= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,) 
    medicine_name = models.CharField(max_length=255)  
    medicine = models.ForeignKey('catalog.MedicineDetails', null=True, blank=True, on_delete=models.SET_NULL) 
    status = models.CharField(max_length = 20, choices=Status.choices, default=Status.PENDING)
    pharmacy = models.ForeignKey('pharmacies.PharmacyDetails',null=True , blank=True , on_delete=models.SET_NULL,)
    created_at = models.DateTimeField(auto_now_add = True)