from django.urls import path

from measurement.views import SensorUpdateRetrieve
from measurement.views import MeasurementCreate
from measurement.views import ShortListSensors
from measurement.views import SensorCreate
from measurement.views import DetailListSensors

urlpatterns = [
    path('detail_list_sensors/', DetailListSensors.as_view()),
    path('sensor_create/', SensorCreate.as_view()),
    path('sensor_update_retrieve/<pk>/', SensorUpdateRetrieve.as_view()),
    path('measurement_create/', MeasurementCreate.as_view()),
    path('short_list_sensors/', ShortListSensors.as_view()),
]
