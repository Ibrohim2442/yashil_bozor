from django.contrib import admin
from .models import Service, Region, Garden, GardenWork


admin.site.register(Service)
admin.site.register(Region)
admin.site.register(Garden)
admin.site.register(GardenWork)