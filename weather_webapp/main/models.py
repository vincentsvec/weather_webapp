from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from django.db.models.signals import post_save
from django.dispatch import receiver


class User_data(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user_data')
    weather_unit = models.CharField(max_length=10, default='metric')
    saved_cities = ArrayField(models.CharField(
        max_length=50, blank=True), size=8, default=list, null=True)
    location = ArrayField(models.CharField(
        max_length=30, blank=True, null=True), size=2, default=None, null=True)


@receiver(post_save, sender=User)
def create_data(sender, instance, created, **kwargs):
    if created:
        User_data.objects.create(user=instance)
