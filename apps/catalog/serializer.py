from rest_framework import serializers
from .models import Category, Seller


class CategorySerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField()
    class Meta:
        model = Category
        fields = ("id", "name", "image", "children")

    def get_children(self, obj):
        children = obj.children.all()
        return [
            {
                "id": c.id,
                "name": c.name,
                "image": c.image.url if c.image else None
            }
            for c in children
        ]


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "name")


class CategoryDetailSerializer(serializers.ModelSerializer):
    children = CategoryListSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ("id", "name", "children")


class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller
        fields = ("id", "name", "description")