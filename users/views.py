from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance
from .models import PharmacyDetails



