from rest_framework import serializers

from apps.services.models import Service, Garden, Region, GardenWork


class ChildServiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Service
        fields = ("id", "name", "image")


class ParentServiceSerializer(serializers.ModelSerializer):

    children = ChildServiceSerializer(many=True, read_only=True)

    class Meta:
        model = Service
        fields = ("id", "name", "children")


# ------------------------------------------------------


class RegionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Region
        fields = ("id", "name")


class GardenWorkSerializer(serializers.ModelSerializer):

    class Meta:
        model = GardenWork
        fields = ("id", "image")


class GardenSerializer(serializers.ModelSerializer):

    region = RegionSerializer(read_only=True)

    class Meta:
        model = Garden
        fields = (
            "id",
            "full_name",
            "experience",
            "region",
            "profile_image",
        )


class GardenDetailSerializer(serializers.ModelSerializer):

    region = RegionSerializer(read_only=True)
    services = ChildServiceSerializer(many=True, read_only=True)
    works = GardenWorkSerializer(many=True, read_only=True)

    class Meta:
        model = Garden
        fields = (
            "id",
            "full_name",
            "profile_image",
            "region",
            "experience",
            "about_me",
            "my_services",
            "services",
            "works",
        )