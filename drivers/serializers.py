from rest_framework import serializers

from .models import Driver


class DriverSerializer(serializers.ModelSerializer):
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    class Meta:
        model = Driver
        fields = ("first_name", "last_name", "created_at", "updated_at")

    def get_created_at(self, obj):
        return obj.created_at.strftime("%d/%m/%Y %H:%M:%S")

    def get_updated_at(self, obj):
        return obj.updated_at.strftime("%d/%m/%Y %H:%M:%S")
