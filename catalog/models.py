from django.db import models

# Create your models here.

class Manufacturer(models.Model):
    name = models.CharField(max_length = 200, unique = True, blank = False, null = False)
    description = models.TextField(blank=True)
    address = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length = 200, unique = True, blank = False, null = False)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = "Categories"

    def ___str__(self):
        return self.name
        
class MedicineDetails(models.Model):
    name = models.CharField(max_length = 200, unique = True, blank = False, null = False)
    synomps = models.TextField(blank = True)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, blank = False, null = False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank = False, null = False)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank = False, null = False)
    dosage_form = models.CharField(max_length=50, blank=True , null=True )  # e.g., 'Tablet', 'Syrup', 'Injection'
    strength = models.CharField(max_length=50, blank=False, null=False)  # e.g., '500 mg', '10 mg/5 ml'

    def __str__(self):
        return f"{self.name} - {self.strength} - {self.dosage_form}" 