from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import PricingConfig, ConfigLog
from threading import local

_user = local()

def set_actor(user):
    _user.value = user

def get_actor():
    return getattr(_user, 'value', None)

@receiver(post_save, sender=PricingConfig)
def log_config_change(sender, instance, created, **kwargs):
    action = "Created" if created else "Updated"
    actor = get_actor()
    ConfigLog.objects.create(config=instance, user=actor, action=action)
