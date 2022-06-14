from django.shortcuts import get_object_or_404

from .filtering_functions import *
from ..models import *

from ..serializers import CarSerializer


def get_all_cars():
    return Car.objects.all()


def delete_car_or_404(pk):
    car = get_object_or_404(Car, pk=pk)
    car.delete()


def update_car_or_404(request, pk):
    car = get_object_or_404(Car, pk=pk)
    serializer = CarSerializer(car, data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return serializer.data


def get_all_statistics():
    return CarDBStatistics.objects.all()


def get_filtered_cars(cars, parameters):
    for key in parameters.keys():
        if key in CARS_FILTERS.keys():
            cars = CARS_FILTERS[key](cars, parameters[key])
        if key[:-2] in CARS_FILTERS.keys():
            cars = CARS_FILTERS[key[:-2]](cars, parameters[key], key[-1])
    return cars
