from django.urls import path
from . import views
from .views import SensorsListView, IndexView, SensorTypesListView

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("sensor/", SensorsListView.as_view(), name="sensor"),
    path("sensor-type/", SensorTypesListView.as_view(), name="sensor_type"),
]