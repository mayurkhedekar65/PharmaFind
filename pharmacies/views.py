from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance
from . models import PharmacyDetails
