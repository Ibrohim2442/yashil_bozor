from rest_framework import generics, permissions
from .models import ProductReview, SellerReview
from .serializer import ProductReviewSerializer, SellerReviewSerializer


class ProductReviewListCreateView(generics.ListCreateAPIView):
    serializer_class = ProductReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return ProductReview.objects.filter(
            product_id=self.kwargs['product_id']
        ).select_related('user').order_by('-created_at')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, product_id=self.kwargs['product_id'])


class ProductReviewDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return ProductReview.objects.filter(product_id=self.kwargs['product_id'])


class SellerReviewListCreateView(generics.ListCreateAPIView):
    serializer_class = SellerReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return SellerReview.objects.filter(
            seller_id=self.kwargs['seller_id']
        ).select_related('user').order_by('-created_at')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, seller_id=self.kwargs['seller_id'])


class SellerReviewDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SellerReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return SellerReview.objects.filter(seller_id=self.kwargs['seller_id'])