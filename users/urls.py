from django.urls import path
from users.views import home_view
path = [
    # Define user-related URL patterns here
    path('', home_view, name='home'),
]