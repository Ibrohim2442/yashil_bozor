from django.urls import path
from .views import CategoryProductsView

urlpatterns = [
    path(
        "categories/<int:category_id>/products/",
        CategoryProductsView.as_view(),
        name="category-products",
    ),
]