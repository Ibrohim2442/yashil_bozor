import django_filters
from .models import Product


class ProductFilter(django_filters.FilterSet):
    price_min = django_filters.NumberFilter(field_name="price", lookup_expr="gte")
    price_max = django_filters.NumberFilter(field_name="price", lookup_expr="lte")

    in_stock = django_filters.BooleanFilter(method="filter_in_stock")
    discount = django_filters.BooleanFilter(method="filter_discount")

    class Meta:
        model = Product
        fields = ["seller", "height", "care", "light"]

    def filter_in_stock(self, queryset, name, value):
        if value:
            return queryset.filter(stock__gt=0)
        return queryset

    def filter_discount(self, queryset, name, value):
        if value:
            return queryset.filter(discount_price__isnull=False)
        return queryset