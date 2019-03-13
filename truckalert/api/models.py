from django.db import models

class Position(models.Model):
    user_id = models.CharField(max_length=255)
    new_long = models.DecimalField(default=0, max_digits=10, decimal_places=8)
    new_lat = models.DecimalField(default=0, max_digits=10, decimal_places=8)
    old_long = models.DecimalField(default=0, max_digits=10, decimal_places=8)
    old_lat = models.DecimalField(default=0, max_digits=10, decimal_places=8)
    prob_ctr = models.IntegerField(default=0)
    alert = models.NullBooleanField(blank=False)


class Event(models.Model):
    event = models.CharField(max_length=255)
    longitude = models.DecimalField(default=0, max_digits=10, decimal_places=8)
    latitude = models.DecimalField(default=0, max_digits=10, decimal_places=8)
    user_id = models.CharField(max_length=255)
    date_added = models.DateTimeField(auto_now_add=True)

