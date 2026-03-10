from django.urls import path

from . import views
from .views import CreateUserView, UserProfileCreateView, UserProfileDetailUpdateView

urlpatterns = [
    path('', CreateUserView.as_view()),

    path('profiles/', UserProfileCreateView.as_view()),
    path('profiles/me/', UserProfileDetailUpdateView.as_view())
]