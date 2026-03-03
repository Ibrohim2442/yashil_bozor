from django.urls import path
from .views import CategoryProductsView, ProductsListView

urlpatterns = [
    path("", ProductsListView.as_view()),
    path("categories/<int:category_id>/", CategoryProductsView.as_view()),
]