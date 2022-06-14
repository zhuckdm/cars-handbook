from carshandbook.serializers import CarDatabaseStatisticsSerializer


def add_statistic_message(message_type, car_data):
    data = {
        'type': message_type,
        'car_data': car_data
    }
    serializer = CarDatabaseStatisticsSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
