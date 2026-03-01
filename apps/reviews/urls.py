from django.urls import path
from .views import (
    ProductReviewListCreateView,
    ProductReviewDetailView,
    SellerReviewListCreateView,
    SellerReviewDetailView,
)

urlpatterns = [
    # Product reviews
    path('products/<int:product_id>/reviews/', ProductReviewListCreateView.as_view()),
    path('products/<int:product_id>/reviews/<int:pk>/', ProductReviewDetailView.as_view()),

    # Seller reviews
    path('sellers/<int:seller_id>/reviews/', SellerReviewListCreateView.as_view()),
    path('sellers/<int:seller_id>/reviews/<int:pk>/', SellerReviewDetailView.as_view()),
]