from rest_framework import status, permissions
from rest_framework.response import Response
# Create your views here.
from rest_framework.views import APIView

from apiApp.models import Sensor, SensorType, WorkingTable, AreaType, Area
from apiApp.serializers import SensorSerializer, SensorTypeSerializer, LoggingSerializer, \
    AreaTypeSerializer, AreaSerializer  # , CreateSensorSerializer


class IndexView(APIView):

    def get(self, request):
        return Response({"message": "Hello World!"})

    pass


class SensorTypeListView(APIView):
    def get(self, request):
        sensor_types = SensorType.objects.all()
        serializer = SensorTypeSerializer(sensor_types, many=True)
        return Response(serializer.data)
        pass

    def post(self, request):
        serializer = SensorTypeSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        pass

    pass


class SensorListView(APIView):
    def get(self, request):
        sensors = Sensor.objects.all()
        serializer = SensorSerializer(sensors, many=True)
        return Response(serializer.data)
        pass

    def post(self, request):
        serializer = SensorSerializer(data=request.data, many=True)
        if serializer.is_valid():
            sensor = serializer.save()
            # serializer = SensorSerializer(sensor)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        pass

    pass


class AreaTypeListView(APIView):
    def get(self, request):
        area_types = AreaType.objects.all()
        serializer = AreaTypeSerializer(area_types, many=True)
        return Response(serializer.data)
        pass

    def post(self, request):
        serializer = AreaTypeSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        pass

    pass


class AreaListView(APIView):
    def get(self, request):
        areas = Area.objects.all()
        serializer = AreaSerializer(areas, many=True)
        return Response(serializer.data)
        pass

    def post(self, request):
        serializer = AreaSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        pass
    pass


class LoggingAPIView(APIView):
    def get(self, request):
        logs = WorkingTable.objects.all()
        serializer = LoggingSerializer(logs, many=True)
        return Response(serializer.data)
        pass

    def post(self, request):
        serializer = LoggingSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
            pass
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        pass

    pass
