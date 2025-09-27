from django.db import models
from catalog.models import MedicineDetails
from pharmacies.models import PharmacyDetails
# Create your models here.
class Availability(models.Model):
    pharmacy = models.ForeignKey(PharmacyDetails, on_delete=models.CASCADE)
    medicine = models.ForeignKey(MedicineDetails, on_delete=models.CASCADE)
    stock_quantity = models.PositiveIntegerField(default = 0)
    price = models.DecimalField(max_digits=10, decimal_places=2, null = True, blank = True)
    updated_at = models.DateTimeField(auto_now = True)

    class META():
        cunique_together = ('pharmacy', 'medicine')
        verbose_name_plural = "Availabilities"

    def __str__(self):
        return f"{self.medicine.name} at {self.pharmacy.name}: {self.stock_quantity}"



