from rest_framework import serializers

from .models import *


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'


class CarDatabaseStatisticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarDBStatistics
        fields = '__all__'
