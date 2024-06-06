from django.urls import path
from .views import grice_details_view

urlpatterns = [
    path('grice-details/', grice_details_view, name='grice-details'),
]
