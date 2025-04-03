from django.contrib import admin
from django.urls import path, include
# from home.views import home_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("home.urls")),  # Home Page
    path("destinations/", include("destinations.urls")),  # Destinations Page
    # path("", home_view, name="home"),

]

