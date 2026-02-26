from django.conf import settings
from django.db import models

from apps.catalog.models import Category, Seller


class Product(models.Model):
    HEIGHT_CHOICES = (
        ("S", "up to 30 cm"),
        ("M", "30–70 cm"),
        ("L", "70–150 cm"),
        ("XL", "above 150 cm"),
    )

    CARE_CHOICES = (
        ("easy", "easy"),
        ("medium", "medium"),
        ("hard", "complex"),
    )

    LIGHT_CHOICES = (
        ("sun", "sun"),
        ("shade", "shade"),
        ("half", "partial shade"),
    )

    name = models.CharField(max_length=255)
    description = models.TextField()

    price = models.DecimalField(max_digits=12, decimal_places=2)
    discount_price = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        null=True,
        blank=True
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="products"
    )

    seller = models.ForeignKey(
        Seller,
        on_delete=models.CASCADE,
        related_name="products"
    )

    stock = models.PositiveIntegerField(default=0)

    height = models.CharField(
        max_length=2,
        choices=HEIGHT_CHOICES,
        blank=True
    )

    care = models.CharField(
        max_length=10,
        choices=CARE_CHOICES,
        blank=True
    )

    light = models.CharField(
        max_length=10,
        choices=LIGHT_CHOICES,
        blank=True
    )

    delivery_days = models.PositiveIntegerField(default=3)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    @property
    def discount_percent(self):
        if self.discount_price and self.price:
            return int((self.price - self.discount_price) / self.price * 100)
        return 0

    @property
    def is_in_stock(self):
        return self.stock > 0


class ProductImage(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="images"
    )
    image = models.ImageField(upload_to="products/")
    is_main = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        images = ProductImage.objects.filter(product=self.product)
        if images.count() == 1 and not self.is_main:
            self.is_main = True
            super().save(update_fields=['is_main'])


class Favorite(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="favorites"
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="favorites"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'product')

    def __str__(self):
        return f"{self.user} → {self.product}"