from rest_framework import serializers
from .models import Category


class CategoryNestedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "name", "image")


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "name")


class CategoryDetailSerializer(serializers.ModelSerializer):
    children = CategoryNestedSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ("id", "name", "image", "children", "is_root", "is_leaf")