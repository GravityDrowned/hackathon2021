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


# class CreateSensorSerializer(serializers.Serializer):
#     type = serializers.CharField(max_length=10, required=True)  # meant to be the SensorType code with which you create a new sensor
#
#     def create(self, validated_data):
#         code = validated_data.get("type")
#         sensor_type = get_object_or_404(SensorType, code=code)
#         return Sensor.objects.create(type=sensor_type)
#         pass
#     pass


class LoggingSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkingTable
        fields = "__all__"

    pass
