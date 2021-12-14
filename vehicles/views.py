from rest_framework import status, viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from drivers.models import Driver

from .models import Vehicle
from .serializers import VehicleSerializer


class VehicleViewSet(viewsets.ModelViewSet):
    """
    A simple ModelViewSet for listing by query parameter and CRUD for Drivers.
    """

    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    lookup_field = "vehicle_id"

    def list(self, request, *args, **kwargs):

        queryset = self.filter_queryset(self.get_queryset())
        with_drivers = request.query_params.get("with_drivers", None)

        if with_drivers == "yes":
            queryset = queryset.exclude(driver=None)

        if with_drivers == "no":
            queryset = queryset.filter(driver=None)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class SetDriverView(APIView):
    """
    A simple APIView for setting a driver to a vehicle.
    """

    serializer_class = VehicleSerializer

    def post(self, request, vehicle_id):
        """
        Set or Unset a driver for a vehicle.
        """
        vehicle = get_object_or_404(Vehicle, id=vehicle_id)
        driver_id = request.data.get("driver_id", None)

        if driver_id:  # we want to set a driver to vehicle
            if vehicle.driver is None:
                driver = Driver.objects.filter(id=driver_id).first()
                if driver:
                    vehicle.driver = driver
                    vehicle.save()
                    serializer = self.serializer_class(vehicle)
                    message = "Vehicle driver set."
                    return Response({"success": message, "data": serializer.data}, status=status.HTTP_200_OK)
                return Response({"error": "Not Found"}, status=status.HTTP_404_NOT_FOUND)
            return Response({"error": "Vehicle already has a driver."}, status=status.HTTP_400_BAD_REQUEST)

        else:  # we want to unset the driver from vehicle
            if vehicle.driver:
                vehicle.driver = None
                vehicle.save()
                serializer = self.serializer_class(vehicle)
                message = "Vehicle driver unset."
                return Response({"success": message, "data": serializer.data}, status=status.HTTP_200_OK)

            return Response({"error": "Vehicle has no driver"}, status=status.HTTP_400_BAD_REQUEST)
