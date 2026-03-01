from django.urls import path
from apps.cart.views import CartDetailView, AddToCartView, UpdateCartItemView, RemoveCartItemView

urlpatterns = [
    path("", CartDetailView.as_view()),
    path("add/", AddToCartView.as_view()),
    path("item/<int:pk>/", UpdateCartItemView.as_view()),
    path("item/<int:pk>/", RemoveCartItemView.as_view()),
]