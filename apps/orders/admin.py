from django import forms
from django.contrib import admin
from django.core.exceptions import ValidationError

from .models import Order, OrderItem, OrderItemReview


class OrderItemInlineForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = '__all__'

    def clean_quantity(self):
        quantity = self.cleaned_data.get('quantity')
        product = self.cleaned_data.get('product')

        if not product or quantity is None:
            return quantity

        old_quantity = 0
        if self.instance and self.instance.pk:
            old_quantity = OrderItem.objects.filter(pk=self.instance.pk).values_list('quantity', flat=True).first() or 0

        delta = quantity - old_quantity
        if delta > 0 and product.stock < delta:
            raise ValidationError(
                f'Insufficient stock for "{product.name}". Only {product.stock} items available.'
            )

        return quantity


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1
    readonly_fields = ("price",)
    form = OrderItemInlineForm


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "recipient_name",
        "total_price",
        "status",
        "created_at",
    )
    list_filter = ("status",)
    search_fields = ("recipient_name", "recipient_phone")
    readonly_fields = ("total_price", "created_at", "latitude", "longitude")
    inlines = (OrderItemInline,)

    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)

        for instance in instances:
            if hasattr(instance, "product") and not instance.price:
                instance.price = instance.product.price

            instance.save()

        formset.save_m2m()

        order = form.instance
        order.total_price = sum(
            item.price * item.quantity for item in order.items.all()
        )
        order.save(update_fields=["total_price"])


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ("id", "order", "product", "quantity", "price")
    readonly_fields = ("price",)

    def has_add_permission(self, request):
        return False

    def has_edit_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

@admin.register(OrderItemReview)
class OrderItemReviewAdmin(admin.ModelAdmin):
    list_display = ("order_item", "rating", "pros", "cons", "comment", "created_at")