from django.urls import path
from measurement.views import AddSensor, UpdateSensor, AddMeasurement, ListSensors, GetSensor

urlpatterns = [
    path('sensors/add', AddSensor.as_view()),
    path('sensors/update/<pk>', UpdateSensor.as_view()),
    path('sensors/measurement', AddMeasurement.as_view()),
    path('sensors/all', ListSensors.as_view()),
    path('sensors/details/<pk>', GetSensor.as_view()),
]
