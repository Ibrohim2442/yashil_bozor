from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from apps.users.models import User, UserProfile, Address


class AddressInline(admin.TabularInline):
    model = Address
    extra = 1
    readonly_fields = ()
    fields = ("city", "street", "house", "apartment", "is_default")


# 🔹 UserProfile Admin
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("id", "first_name", "last_name", "phone")
    search_fields = ("first_name", "last_name", "user__phone")
    inlines = [AddressInline]


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    model = User
    list_display = ("id", "phone", "is_staff", "is_active")
    ordering = ("id",)
    fieldsets = (
        (None, {"fields": ("phone", "password")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "is_superuser", "groups", "user_permissions")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("phone", "password1", "password2", "is_staff", "is_active"),
        }),
    )


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ("id", "profile", "city", "street", "house", "is_default")
    list_filter = ("city", "is_default")
    search_fields = ("city", "street", "profile__first_name", "profile__last_name")