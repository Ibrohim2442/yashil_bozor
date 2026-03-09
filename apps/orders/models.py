from django.conf import settings
from django.db import models
from geopy.geocoders import Nominatim

from apps.products.models import Product


# Create your models here.

class Order(models.Model):

    STATUS_CHOICES = (
        ("pending", "Pending"),
        ("paid", "Paid"),
        ("processing", "Processing"),
        ("delivered", "Delivered"),
        ("cancelled", "Cancelled"),
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="orders"
    )

    recipient_name = models.CharField(max_length=255)
    recipient_phone = models.CharField(max_length=20)

    courier_note = models.TextField(blank=True)

    address = models.CharField(max_length=100)

    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    total_price = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="pending"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):

        if self.latitude is None or self.longitude is None:
            geolocator = Nominatim(user_agent="apps")
            location = geolocator.geocode(self.address)

            if location is not None:
                print(location.longitude, location.latitude)
                print(location.raw)

                self.latitude = location.latitude
                self.longitude = location.longitude

        super().save(*args, **kwargs)


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name="items"
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=12, decimal_places=2)