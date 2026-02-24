from django.urls import path

from . import views
from .views import CreateUserProfileView, CreateUserView

urlpatterns = [
    path('user/create/', CreateUserView.as_view()),
    path('profile/create/', CreateUserProfileView.as_view())
]