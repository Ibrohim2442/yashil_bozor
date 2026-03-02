from rest_framework import serializers

from apps.services.models import ChildService, ParentService, Garden, Region

class ChildServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChildService
        fields = ('name', 'image',)

class ParentServiceSerializer(serializers.ModelSerializer):
    children = ChildServiceSerializer(many=True, read_only=True)

    class Meta:
        model = ParentService
        fields = ('id', 'name', 'children')

# --------------------------------------------------

class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ('name',)

class GardenSerializer(serializers.ModelSerializer):
    region = RegionSerializer(read_only=True)
    # services = ChildServiceSerializer(read_only=True)

    class Meta:
        model = Garden
        fields = ('id', 'full_name', 'experience', 'region', 'profile_image',)

class GardenDetailSerializer(serializers.ModelSerializer):
    region = RegionSerializer(read_only=True)

    class Meta:
        model = Garden
        fields = ('id', 'full_name', 'profile_image', 'region', 'experience', 'about_me', 'my_works', 'my_services')