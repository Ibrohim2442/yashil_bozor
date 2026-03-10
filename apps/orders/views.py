from django.template.context_processors import request
from rest_framework import generics, permissions
from .models import Order, OrderItemReview
from .serializers import OrderSerializer, OrderItemReviewSerializer, OrderCreateSerializer


class OrderListCreateView(generics.ListCreateAPIView):
    # serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user).prefetch_related('items').order_by('-created_at')

    def get_serializer_class(self): # what is inside self
        # print(self)
        # print(self.request.method)
        if self.request.method == 'POST':
            return OrderCreateSerializer
        return OrderSerializer


class OrderDetailView(generics.RetrieveAPIView):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user).prefetch_related('items')

class OrderItemReviewView(generics.ListCreateAPIView):
    queryset = OrderItemReview.objects.all()
    serializer_class = OrderItemReviewSerializer
    permission_classes = [permissions.IsAuthenticated]