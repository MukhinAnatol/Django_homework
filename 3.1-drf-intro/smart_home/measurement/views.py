# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, RetrieveAPIView
from measurement.models import Sensor, Measurement
from measurement.serializers import MeasurementSerializer, SensorSerializer, SensorDetailSerializer


class AddSensor(CreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

class ListSensors(ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

class UpdateSensor(UpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

class AddMeasurement(CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer


class GetSensor(RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer
