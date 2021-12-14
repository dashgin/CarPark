from rest_framework import status, viewsets
from rest_framework.response import Response

from .models import Driver
from .serializers import DriverSerializer
from .utils import string_to_date


class DriverViewSet(viewsets.ModelViewSet):
    """
    A simple ModelViewSet for listing by query parameter and CRUD for Drivers.
    """

    queryset = Driver.objects.all()
    serializer_class = DriverSerializer
    lookup_field = "driver_id"

    def list(self, request, *args, **kwargs):

        queryset = self.filter_queryset(self.get_queryset())
        created_at__gte = request.query_params.get("created_at__gte", None)
        created_at__lte = request.query_params.get("created_at__lte", None)

        if created_at__gte:
            filter_date = string_to_date(created_at__gte)
            queryset = queryset.filter(created_at__date__gte=filter_date)

        if created_at__lte:
            filter_date = string_to_date(created_at__lte)
            queryset = queryset.filter(created_at__date__lte=filter_date)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
