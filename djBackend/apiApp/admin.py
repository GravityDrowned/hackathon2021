from django.contrib import admin

# Register your models here.
from apiApp.models import Area, AreaType, SensorType, Sensor, WorkingTable

admin.site.register(AreaType)
admin.site.register(Area)
admin.site.register(SensorType)
admin.site.register(Sensor)
admin.site.register(WorkingTable)
