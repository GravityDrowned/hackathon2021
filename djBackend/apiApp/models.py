from django.db import models
from django.utils import timezone
import uuid

# Create your models here.


class AreaType(models.Model):
    type = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=30, unique=True)
    max_capacity = models.IntegerField()

    def __str__(self):
        return f"{self.name} | {self.type} | Max Capacity: {self.max_capacity}"
        pass
    pass


class Area(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    floor = models.CharField(max_length=10)
    type = models.ForeignKey(AreaType, on_delete=models.CASCADE)
    sensors = models.JSONField()  # a list of sensors in the given area in a floor; list of all IDs of the sensors

    def __str__(self):
        return f"{self.name} | {self.type.type}"
        pass
    pass


class SensorType(models.Model):
    type = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=30, unique=True)
    unit = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.type} | {self.name} | Measurement Unit: {self.unit}"
        pass
    pass


class Sensor(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    type = models.ForeignKey(SensorType, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id} | {self.type.type}"
        pass
    pass


class WorkingTable(models.Model):
    timestamp = models.DateTimeField(default=timezone.now)
    area = models.ForeignKey(Area, on_delete=models.DO_NOTHING)
    sensor = models.ForeignKey(Sensor, on_delete=models.DO_NOTHING)
    sensor_value = models.FloatField()
    pass
