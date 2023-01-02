from django.urls import path
from measurement.views import AddMeasurement, SensorsView, SensorGetView

urlpatterns = [
    path('sensors/view', SensorsView.as_view()),
    path('sensors/measurement', AddMeasurement.as_view()),
    path('sensors/detailed/<pk>', SensorGetView.as_view()),
]
