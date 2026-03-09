from django.urls import path

from . import views
from .views import CreateUserView, UserProfileCreateView, UserProfileDetailView, UserProfileUpdateView

urlpatterns = [
    path('users/', CreateUserView.as_view()),

    path('profiles/', UserProfileCreateView.as_view()),
    path('profiles/me/', UserProfileDetailView.as_view()),
    path('profiles/me/', UserProfileUpdateView.as_view()),
]