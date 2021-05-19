from django.urls import path
from . import views
from .views import SensorListView, IndexView, SensorTypeListView, LoggingAPIView, AreaTypeListView, AreaListView

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("sensor-type/", SensorTypeListView.as_view(), name="sensor_type"),
    path("sensor/", SensorListView.as_view(), name="sensor"),
    path("area-type/", AreaTypeListView.as_view(), name="area_type"),
    path("area/", AreaListView.as_view(), name="area"),
    path("log/", LoggingAPIView.as_view(), name="logging"),
]
