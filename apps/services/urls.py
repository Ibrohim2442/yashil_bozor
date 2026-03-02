from django.urls import path

from .views import ListServiceView, GardenListView, GardenDetailView

urlpatterns = [
    path('', ListServiceView.as_view()),

    path('gardens/', GardenListView.as_view())
    ,
    path('gardens/<int:pk>/', GardenDetailView.as_view())
]