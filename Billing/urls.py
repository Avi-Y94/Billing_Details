from django.urls import path
from .views import PriceCalculationView

urlpatterns = [
    path('calculate-price/', PriceCalculationView.as_view(), name='calculate-price'),
]
