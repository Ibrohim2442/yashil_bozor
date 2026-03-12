from django.core.exceptions import ValidationError
from django.db import models


class Service(models.Model):
    name = models.CharField(max_length=255)

    parent = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="children"
    )

    image = models.ImageField(
        upload_to="services/",
        null=True,
        blank=True
    )

    def clean(self):
        if self.parent is None and self.image:
            raise ValidationError("Parent service cannot have an image.")

        if self.parent is not None and not self.image:
            raise ValidationError("Child service must have an image.")

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        if self.parent:
            return f"{self.parent.name} → {self.name}"
        return self.name


# ------------------------------------------------------------


class Region(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Garden(models.Model):
    full_name = models.CharField(max_length=255)

    profile_image = models.ImageField(upload_to="gardens/")

    region = models.ForeignKey(
        Region,
        on_delete=models.SET_NULL,
        null=True,
        related_name="gardens"
    )

    experience = models.PositiveIntegerField()

    about_me = models.TextField()

    my_services = models.TextField()

    services = models.ManyToManyField(
        Service,
        related_name="gardens"
    )

    def __str__(self):
        return self.full_name


class GardenWork(models.Model):
    garden = models.ForeignKey(
        Garden,
        on_delete=models.CASCADE,
        related_name="works"
    )

    image = models.ImageField(upload_to="gardens/works/")

    def __str__(self):
        return f"Work of {self.garden.full_name}"