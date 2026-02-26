from django.contrib import admin

from .models import User, UserProfile, Address

# admin.site.register(User)
admin.site.register(UserProfile)
# admin.site.register(Address)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    fields = ('phone',)

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    readonly_fields = ('latitude', 'longitude')