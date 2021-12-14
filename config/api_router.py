from django.urls import include, path

urlpatterns = [
    path("vehicles/", include("vehicles.urls")),
    path("drivers/", include("drivers.urls")),
]
