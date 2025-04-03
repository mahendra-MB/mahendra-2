from django.urls import path
from .views import home_view, register_view, login_view, destinations_view, logout_view

urlpatterns = [
    path("", home_view, name="home"),
    path("register/", register_view, name="register"),
    path("login/", login_view, name="login"),
    path("destinations/", destinations_view, name="destinations"),
    path("logout/", logout_view, name="logout"),  # ✅ Logout URL added
]
