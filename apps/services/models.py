from django.db import models

# Create your models here.

class ParentService(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class ChildService(models.Model):
    parent = models.ForeignKey(
        ParentService,
        on_delete=models.CASCADE,
        related_name="children"
    )
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to="services/")

    def __str__(self):
        return f"{self.parent.name} → {self.name}"

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
    my_works = models.ImageField('gardens/works/')
    my_services = models.TextField()

    services = models.ManyToManyField(
        ChildService,
        related_name="gardens"
    )

    def __str__(self):
        return self.full_name