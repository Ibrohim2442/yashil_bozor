from rest_framework import generics
from rest_framework.generics import ListAPIView

from apps.services.models import Service, Garden
from apps.services.serializers import (
    ParentServiceSerializer,
    GardenSerializer,
    GardenDetailSerializer,
)


class ListServiceView(ListAPIView):

    serializer_class = ParentServiceSerializer

    queryset = Service.objects.filter(
        parent__isnull=True
    ).prefetch_related("children")


# -------------------------------------------------------------


class GardenListView(ListAPIView):

    serializer_class = GardenSerializer

    queryset = Garden.objects.select_related(
        "region"
    ).prefetch_related(
        "services"
    )

    filterset_fields = ("region", "services")


class GardenDetailView(generics.RetrieveAPIView):

    serializer_class = GardenDetailSerializer

    queryset = Garden.objects.select_related(
        "region"
    ).prefetch_related(
        "services",
        "works"
    )