from django.contrib import admin

from apps.services.models import Garden, Region, ChildService, ParentService

# Register your models here.
# @admin.register(ModelName)
# class ModelNameAdmin(admin.ModelAdmin):

admin.site.register(ParentService)
admin.site.register(ChildService)
admin.site.register(Region)
admin.site.register(Garden)