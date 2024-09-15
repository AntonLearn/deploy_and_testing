from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from measurement.models import Sensor, Measurement
from measurement.serializers import CreateMeasurementSerializer
from measurement.serializers import SensorCreateSerializer
from measurement.serializers import ShortListSensorsSerializer
from measurement.serializers import SensorUpdateRetrieveSerializer


class SensorCreate(ListCreateAPIView):
    """Создать датчик. Указываются название и описание датчика. Final version!"""
    queryset = Sensor.objects.all()
    serializer_class = SensorCreateSerializer


class ShortListSensors(ListCreateAPIView):
    """Получить список датчиков. Выдается список с краткой информацией по датчикам:
    ID, название и описание"""
    queryset = Sensor.objects.all()
    serializer_class = ShortListSensorsSerializer


class SensorUpdateRetrieve(RetrieveUpdateAPIView):
    """Получить информацию по конкретному датчику.
    ID, название, описание и список всех измерений с температурой и временем"""
    queryset = Sensor.objects.all()
    serializer_class = SensorUpdateRetrieveSerializer


class MeasurementCreate(CreateAPIView):
    """Добавить измерение. Указываются ID датчика и температура"""
    queryset = Measurement.objects.all()
    serializer_class = CreateMeasurementSerializer


class DetailListSensors(ListCreateAPIView):
    """Получить список датчиков. Выдается список с полной информацией по датчикам:
    ID, название, описание, измерения"""
    queryset = Sensor.objects.all()
    serializer_class = SensorUpdateRetrieveSerializer
