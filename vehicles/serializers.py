from rest_framework import serializers

from .models import Vehicle


class VehicleSerializer(serializers.ModelSerializer):
    driver = serializers.StringRelatedField(read_only=True)
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    class Meta:
        model = Vehicle
        fields = ("id", "driver", "make", "model", "plate_number", "created_at", "updated_at")

    def get_created_at(self, obj):
        return obj.created_at.strftime("%d/%m/%Y %H:%M:%S")

    def get_updated_at(self, obj):
        return obj.updated_at.strftime("%d/%m/%Y %H:%M:%S")
