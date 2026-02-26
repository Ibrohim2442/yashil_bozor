from rest_framework import generics

from apps.catalog.models import Category
from apps.catalog.serializer import CategoryDetailSerializer, CategoryListSerializer


# Create your views here.

class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.filter(parent__isnull=True)
    serializer_class = CategoryListSerializer


class CategoryDetailView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerializer