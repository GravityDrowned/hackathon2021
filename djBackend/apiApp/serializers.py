from rest_framework import serializers

from apiApp.models import AreaType, Area, SensorType, Sensor, WorkingTable


class AreaTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AreaType
        fields = "__all__"
    pass


class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = "__all__"
    pass


class SensorTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorType
        fields = "__all__"
    pass


class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = "__all__"
    pass


class WorkingTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkingTable
        fields = "__all__"
    pass
