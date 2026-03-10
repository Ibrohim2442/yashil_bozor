from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms.models import BaseInlineFormSet
from django.utils.html import format_html

from apps.products.models import Product, ProductImage, Favorite, Seller


@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)

class ProductImageInlineFormSet(BaseInlineFormSet):
    def clean(self):
        super().clean()

        images = [
            form.cleaned_data
            for form in self.forms
            if form.cleaned_data and not form.cleaned_data.get("DELETE", False)
        ]

        if not images:
            raise ValidationError("At least one image must be added for the product.")

        main_images = [img for img in images if img.get("main")]

        if not main_images:
            if len(images) == 1:
                images[0]["main"] = True
            else:
                raise ValidationError("At least one image must be marked as main.")


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    formset = ProductImageInlineFormSet
    extra = 1
    readonly_fields = ("image_preview",)

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50"/>', obj.image.url)
        return "-"
    image_preview.short_description = "Preview"


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "category",
        "seller",
        "price",
        "discount_price",
        "stock",
        "is_in_stock",
    )
    list_filter = ("category", "seller", "height", "care", "light")
    search_fields = ("name", "description")
    inlines = (ProductImageInline,)

    def is_in_stock(self, obj):
        return obj.stock > 0
    is_in_stock.boolean = True
    is_in_stock.short_description = "In Stock"


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ("user", "product", "created_at")
    list_filter = ("created_at",)
    search_fields = ("user__phone", "product__name")