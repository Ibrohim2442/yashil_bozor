from django.shortcuts import render
from rest_framework import generics
from rest_framework.generics import ListAPIView

from apps.services.models import ParentService, Garden
from apps.services.serializer import ParentServiceSerializer, GardenSerializer, GardenDetailSerializer


# Create your views here.

class ListServiceView(generics.ListAPIView):
    queryset = ParentService.objects.all()
    serializer_class = ParentServiceSerializer

# -------------------------------------------------------------------------

class GardenListView(generics.ListAPIView):
    queryset = Garden.objects.all()
    serializer_class = GardenSerializer
    filterset_fields = ('region__name', 'services__name')

class GardenDetailView(generics.RetrieveAPIView):
    queryset = Garden.objects.all()
    serializer_class = GardenDetailSerializer