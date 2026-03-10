from rest_framework import generics

from apps.categories.models import Category
from apps.categories.serializers import CategoryDetailSerializer, CategoryListSerializer


# Create your views here.

class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.prefetch_related('children').filter(parent__isnull=True)
    serializer_class = CategoryListSerializer


class CategoryDetailView(generics.RetrieveAPIView):
    queryset = Category.objects.prefetch_related('children').all()
    serializer_class = CategoryDetailSerializer