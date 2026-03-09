from django.urls import path
from .views import OrderListCreateView, OrderDetailView, OrderItemReviewView

urlpatterns = [
    path('', OrderListCreateView.as_view()),
    path('<int:pk>/', OrderDetailView.as_view()),
    path('<int:pk>/reviews/', OrderItemReviewView.as_view()),
]