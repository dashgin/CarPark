from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import SetDriverView, VehicleViewSet

router = DefaultRouter()
router.register("vehicle", VehicleViewSet, basename="vehicle")

urlpatterns = [
    path("", include(router.urls)),
    path("set_driver/<int:vehicle_id>/", SetDriverView.as_view(), name="set-driver"),
]
