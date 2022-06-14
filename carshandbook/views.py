from rest_framework import generics
from rest_framework.response import Response

from .services.api_services import *
from .services.statistic_message_services import *


class CarAPIListView(generics.ListCreateAPIView):
    queryset = get_all_cars()
    serializer_class = CarSerializer

    def get(self, request, *args, **kwargs):
        cars = get_all_cars()
        filtered_cars = get_filtered_cars(cars, request.GET)
        return Response(CarSerializer(filtered_cars, many=True).data)

    def post(self, request,  *args, **kwargs):
        serializer = CarSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        add_statistic_message('CREATE', serializer.data)
        return Response(serializer.data, 201)


class CarAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = get_all_cars()
    serializer_class = CarSerializer

    def delete(self, request,  *args, **kwargs):
        pk = kwargs.get("pk", None)
        delete_car_or_404(pk)
        add_statistic_message('DELETE', {'id': pk})
        return Response(None, 204)

    def update(self, request, *args, **kwargs):
        car_data = update_car_or_404(request, kwargs.get("pk", None))
        add_statistic_message('UPDATE', car_data)
        return Response(car_data, 200)


class CarDBStatisticsAPIView(generics.ListAPIView):
    queryset = get_all_statistics()
    serializer_class = CarDatabaseStatisticsSerializer
