from .models import PricingConfig
from decimal import Decimal

def calculate_price(ride_minutes, waiting_minutes, distance_km, day):
    config = PricingConfig.objects.filter(is_active=True).first()
    if not config:
        raise Exception("No active pricing configuration")
    


    # Convert inputs to Decimal
    ride_minutes = Decimal(ride_minutes)
    waiting_minutes = Decimal(waiting_minutes)
    distance_km = Decimal(str(distance_km)) 

    # DBP
    base_price = config.base_prices.filter(day=day.lower(), upto_km__gte=distance_km).order_by('upto_km').first()
    base = base_price.price if base_price else Decimal(0)

    # DAP
    threshold_km = base_price.upto_km if base_price else 0
    additional_km = max(0, distance_km - threshold_km)
    additional_rate = config.additional_prices.first().price_per_km
    dap = additional_km * additional_rate

    # TMF
    tmf = Decimal(1)
    for factor in config.time_multipliers.all():
        if factor.min_minutes <= ride_minutes <= factor.max_minutes:
            tmf = Decimal(factor.multiplier)
            break

    # WC
    wc = Decimal(0)
    if waiting_minutes > config.waiting_charge.after_minutes:
        extra_wait = waiting_minutes - config.waiting_charge.after_minutes
        wc_units = extra_wait // config.waiting_charge.per_minutes
        wc = wc_units * config.waiting_charge.charge

    total_price = (base + dap) * tmf + wc
    return float(total_price)
