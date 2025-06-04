from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

DAYS_OF_WEEK = [
    ('mon', 'Monday'),
    ('tue', 'Tuesday'),
    ('wed', 'Wednesday'),
    ('thu', 'Thursday'),
    ('fri', 'Friday'),
    ('sat', 'Saturday'),
    ('sun', 'Sunday'),
]


class PricingConfig(models.Model):
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({'Active' if self.is_active else 'Inactive'})"


class DistanceBasePrice(models.Model):
    config = models.ForeignKey(PricingConfig, related_name='base_prices', on_delete=models.CASCADE)
    day = models.CharField(max_length=3, choices=DAYS_OF_WEEK)
    upto_km = models.FloatField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.day} - {self.upto_km} km = ₹{self.price}"


class DistanceAdditionalPrice(models.Model):
    config = models.ForeignKey(PricingConfig, related_name='additional_prices', on_delete=models.CASCADE)
    price_per_km = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.price_per_km}/km (Additional)"


class TimeMultiplierFactor(models.Model):
    config = models.ForeignKey(PricingConfig, related_name='time_multipliers', on_delete=models.CASCADE)
    min_minutes = models.IntegerField()
    max_minutes = models.IntegerField()
    multiplier = models.FloatField()

    def __str__(self):
        return f"{self.min_minutes}-{self.max_minutes} mins = x{self.multiplier}"


class WaitingCharge(models.Model):
    config = models.OneToOneField(PricingConfig, related_name='waiting_charge', on_delete=models.CASCADE)
    per_minutes = models.IntegerField()
    after_minutes = models.IntegerField()
    charge = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"₹{self.charge} per {self.per_minutes} mins after {self.after_minutes} mins"


class ConfigLog(models.Model):
    config = models.ForeignKey(PricingConfig, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    action = models.CharField(max_length=100)
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.config.name} - {self.action} by {self.user} at {self.timestamp}"
