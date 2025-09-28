# availability/views.py

from django.shortcuts import render
from .models import Availability
from .utils import haversine

def search_view(request):
    query = request.GET.get('q', '')
    
    # Correctly get lat/lng from the URL query parameters sent by the form.
    try:
        user_lat = float(request.GET.get('lat', '0.0'))
        user_lon = float(request.GET.get('lng', '0.0'))
    except (ValueError, TypeError):
        user_lat, user_lon = 0.0, 0.0

    results = []
    location_error = False

    # Check if the location is the default (0.0, 0.0), which means it wasn't provided.
    if user_lat == 0.0 and user_lon == 0.0:
        location_error = True

    if query:
        availabilities = Availability.objects.select_related('pharmacy', 'medicine').filter(
            medicine__name__icontains=query,
            stock_quantity__gt=0
        )

        results_with_distance = []
        for item in availabilities:
            # Only calculate distance if we have a valid user location
            if not location_error and item.pharmacy and item.pharmacy.latitude is not None and item.pharmacy.longitude is not None:
                distance = haversine(
                    user_lat,
                    user_lon,
                    item.pharmacy.latitude,
                    item.pharmacy.longitude
                )
                item.distance = distance
            else:
                item.distance = None # Set distance to None if no location
            
            results_with_distance.append(item)

        # Sort by distance only if we have a valid location
        if not location_error:
            # Filter out items that couldn't have a distance calculated
            results_with_distance = [item for item in results_with_distance if item.distance is not None]
            results = sorted(results_with_distance, key=lambda item: item.distance)
        else:
            results = results_with_distance # Show results unsorted

    return render(request, 'catalog/search_results.html', {
        'results': results,
        'query': query,
        'location_error': location_error,
    })