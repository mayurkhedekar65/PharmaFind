# from django.db import models
# from django.conf import settings
# from django.contrib.auth.models import User
# #from django.contrib.gis.db import models
# # Create your models here.

# class PharmacyDetails(models.Model):
#     name = models.CharField(max_length =200 , blank=False, null=False)
#     address = models.CharField(max_length = 300, blank = False, null = False)
#     phone = models.CharField(max_length = 20 , blank = True, null = True)
#     email = models.EmailField()
#     opening_hours = models.TextField(help_text="e.g., Mon-Fri: 9am-9pm, Sat: 10am-6pm")
#    # location = models.PointField()
#     latitude = models.FloatField(null = True, blank = True)
#     longitude = models.FloatField(null = True, blank = True)

   

# #Optional: Override save method to auto-update lat/lon from location
#     def save(self, *args, **kwargs):
#         if self.location:
#             self.latitude = self.location.y
#             self.longitude = self.location.x
#             super().save(*args, **kwargs)

#     def __str__(self):
#         return self.name