from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import DriverViewSet

router = DefaultRouter()
router.register("driver", DriverViewSet, basename="driver")

urlpatterns = [
    path("", include(router.urls)),
]
