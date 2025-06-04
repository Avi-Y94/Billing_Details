from django.contrib import admin

from .models import *

class DistanceBasePriceInline(admin.TabularInline):
    model = DistanceBasePrice
    extra = 1

class DistanceAdditionalPriceInline(admin.TabularInline):
    model = DistanceAdditionalPrice
    extra = 1

class TimeMultiplierFactorInline(admin.TabularInline):
    model = TimeMultiplierFactor
    extra = 1

@admin.register(PricingConfig)
class PricingConfigAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_active', 'created_at']
    list_filter = ['is_active']
    inlines = [
        DistanceBasePriceInline,
        DistanceAdditionalPriceInline,
        TimeMultiplierFactorInline,
    ]

@admin.register(WaitingCharge)
class WaitingChargeAdmin(admin.ModelAdmin):
    list_display = ['config', 'per_minutes', 'after_minutes', 'charge']

@admin.register(ConfigLog)
class ConfigLogAdmin(admin.ModelAdmin):
    list_display = ['config', 'user', 'action', 'timestamp']
