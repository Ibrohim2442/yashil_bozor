from django.db import models
from django.core.exceptions import ValidationError


class Category(models.Model):
    name = models.CharField(max_length=255)
    parent = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="children"
    )
    image = models.ImageField(
        upload_to="categories/",
        null=True,
        blank=True
    )

    class Meta:
        verbose_name_plural = "Categories"

    def save(self, *args, **kwargs):
        if self.parent is None:
            self.image = None

        if self.parent and self.parent == self:
            raise ValidationError("Category cannot be its own parent!")

        if self.parent and self.parent.parent is not None:
            raise ValidationError("Child category cannot be a parent!")

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    @property
    def is_root(self):
        return self.parent is None


class Seller(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    logo = models.ImageField(
        upload_to="sellers/",
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name