from django.contrib import admin
from django.core.exceptions import ValidationError
from django.utils.html import format_html

from apps.catalog.models import Category, Seller


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "get_parent_name", "image_preview")
    list_filter = ("parent",)
    search_fields = ("name",)
    readonly_fields = ("image_preview",)

    def get_parent_name(self, obj):
        return obj.parent.name if obj.parent else "-"
    get_parent_name.short_description = "Parent"

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50"/>', obj.image.url)
        return "-"
    image_preview.short_description = "Image"

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)

        queryset = Category.objects.filter(parent__isnull=True)
        if obj:
            queryset = queryset.exclude(pk=obj.pk)

        form.base_fields["parent"].queryset = queryset
        return form

    def save_model(self, request, obj, form, change):
        if obj.parent == obj:
            raise ValidationError("Category cannot be its own parent.")

        if obj.parent and obj.parent.parent:
            raise ValidationError("Child category cannot be a parent.")

        super().save_model(request, obj, form, change)


@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)