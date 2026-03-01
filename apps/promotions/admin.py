from django.contrib import admin

from apps.promotions.models import PromoCode

# Register your models here.

# admin.site.register(PromoCode)
@admin.register(PromoCode)
class PromoCodeAdmin(admin.ModelAdmin):
    fields = ('code', 'discount_percent', 'expire_date', 'max_usage', 'used_count')

    readonly_fields = ('used_count',)