from rest_framework import status, permissions
from rest_framework.response import Response
# Create your views here.
from rest_framework.views import APIView

from apiApp.models import Sensor, SensorType
from apiApp.serializers import SensorSerializer, SensorTypeSerializer


class IndexView(APIView):
    permission_classes = [permissions.AllowAny, ]

    def get(self, request):
        return Response({"message": "Hello World!"})

    pass


class SensorsListView(APIView):
    def get(self, request):
        sensors = Sensor.objects.all()
        serializer = SensorSerializer(sensors, many=True)
        return Response(serializer.data)
        pass

    def post(self, request):
        serializer = SensorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        pass

    pass


class SensorTypesListView(APIView):
    def get(self, request):
        sensor_types = SensorType.objects.all()
        serializer = SensorTypeSerializer(sensor_types, many=True)
        return Response(serializer.data)
        pass

    def post(self, request):
        serializer = SensorTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        pass

    pass
