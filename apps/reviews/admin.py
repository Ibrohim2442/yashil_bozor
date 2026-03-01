from django.contrib import admin

from apps.reviews.models import ProductReview, SellerReview

# Register your models here.

admin.site.register(ProductReview)
admin.site.register(SellerReview)