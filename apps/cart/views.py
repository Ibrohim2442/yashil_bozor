from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from apps.cart.models import CartItem, Cart
from apps.cart.serializers import CartSerializer, CartItemSerializer


# Create your views here.

def get_or_create_cart(user):
    cart, _ = Cart.objects.get_or_create(user=user)
    return cart

class CartDetailView(generics.RetrieveAPIView):
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return get_or_create_cart(self.request.user)

class AddToCartView(generics.CreateAPIView):
    serializer_class = CartItemSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['cart'] = get_or_create_cart(self.request.user)
        return context

class UpdateCartItemView(generics.UpdateAPIView):
    serializer_class = CartItemSerializer
    permission_classes = [IsAuthenticated]
    queryset = CartItem.objects.all()

class RemoveCartItemView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = CartItem.objects.all()
