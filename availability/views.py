# availability/views.py

from django.shortcuts import render
from pharmacies.models import PharmacyDetails as Pharmacy
from .utils import haversine  # <-- Import our new function

def search_view(request):
    query = request.GET.get('q', '')
    
    # Get user's location from URL, default to 0.0 if not provided
    try:
        user_lat = float(request.GET.get('lat', '0.0'))
        user_lon = float(request.GET.get('lng', '0.0'))
    except (ValueError, TypeError):
        user_lat, user_lon = 0.0, 0.0

    results = []

    if query and user_lat and user_lon:
        # 1. Filter pharmacies by name
        pharmacies = Pharmacy.objects.filter(name__icontains=query)

        # 2. Calculate distance for each pharmacy and store as a tuple (pharmacy, distance)
        pharmacies_with_distance = []
        for p in pharmacies:
            distance = haversine(user_lat, user_lon, p.latitude, p.longitude)
            pharmacies_with_distance.append((p, distance))

        # 3. Sort the list of tuples by distance (the second item in the tuple)
        results = sorted(pharmacies_with_distance, key=lambda item: item[1])

    return render(request, 'catalog/search_results.html', {
        'results': results,
        'query': query,
        'user_lat': user_lat, # Pass user's lat/lon to template
        'user_lon': user_lon,
    })