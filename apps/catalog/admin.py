from django.contrib import admin
from django.core.exceptions import ValidationError

from apps.catalog.models import Category, Seller


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent_name', 'image_display')
    list_filter = ('parent',)
    search_fields = ('name',)
    readonly_fields = ('image_display',)

    def parent_name(self, obj):
        return obj.parent.name if obj.parent else '-'
    parent_name.short_description = 'Parent'

    def image_display(self, obj):
        if hasattr(obj, 'image') and obj.image:
            return f'<img src="{obj.image.url}" width="50"/>'
        return '-'
    image_display.allow_tags = True
    image_display.short_description = 'Image'

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        qs = Category.objects.filter(parent__isnull=True)
        if obj:
            qs = qs.exclude(pk=obj.pk)
        form.base_fields['parent'].queryset = qs
        return form

    def save_model(self, request, obj, form, change):
        if obj.parent and obj.parent == obj:
            raise ValidationError('Category cannot be its own parent!')
        if obj.parent and obj.parent.parent is not None:
            raise ValidationError('Child category cannot be a parent!')
        super().save_model(request, obj, form, change)

@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)