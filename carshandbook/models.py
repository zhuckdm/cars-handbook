from django.db import models


class Car(models.Model):
    registration_plate = models.CharField(max_length=255, unique=True, verbose_name='Номер')
    make = models.CharField(max_length=255, verbose_name='Марка')
    model = models.CharField(max_length=255, verbose_name='Модель')
    color = models.CharField(max_length=255, verbose_name='Цвет')
    manufacture_year = models.IntegerField(verbose_name='Год выпуска')
    horsepower = models.IntegerField(verbose_name='Количество лошадиных сил')
    mileage = models.IntegerField(verbose_name='Пробег, км.')
    price = models.IntegerField(verbose_name='Цена, руб.')

    def __str__(self):
        return self.registration_plate

    class Meta:
        verbose_name = 'Автомобиль'
        verbose_name_plural = 'Автомобили'
        ordering = ['registration_plate']


class CarDBStatistics(models.Model):
    type = models.CharField(max_length=255, verbose_name='Тип записи')
    car_data = models.JSONField(verbose_name='Информация об автомобиле', default=None)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата записи')

    class Meta:
        verbose_name = 'Статистика базы автомобилей'
        verbose_name_plural = 'Статистика базы автомобилей'
        ordering = ['time_create']
