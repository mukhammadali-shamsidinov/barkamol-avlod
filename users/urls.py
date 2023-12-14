from django.urls import path
from .views import RegisterView,Login,ProfileView


app_name="users"

urlpatterns = [
    path('register/',RegisterView.as_view(),name="register"),
    path('login/',Login.as_view(),name="login"),
    path('profile/',ProfileView.as_view(),name="profile")
]