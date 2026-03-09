from django.contrib import admin

from .models import User, UserProfile

# admin.site.register(User)
admin.site.register(UserProfile)
# admin.site.register(Address)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    fields = ('phone',)