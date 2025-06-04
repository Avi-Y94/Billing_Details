from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .utils import calculate_price

class PriceCalculationView(APIView):
    def post(self, request):
        try:
            day = request.data.get("day", "").lower()
            ride_minutes = int(request.data.get("ride_minutes"))
            waiting_minutes = int(request.data.get("waiting_minutes"))
            distance_km = float(request.data.get("distance_km"))

            price = calculate_price(ride_minutes, waiting_minutes, distance_km, day)
            return Response({"total_price": round(price, 2)}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
