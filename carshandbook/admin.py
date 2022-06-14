from django.contrib import admin

from .models import *


class CarAdmin(admin.ModelAdmin):
    list_display = ('registration_plate', 'make', 'model', 'price')
    list_display_links = ('registration_plate', )


class CarDBStatisticsAdmin(admin.ModelAdmin):
    list_display = ('type', 'car_data', 'time_create')
    list_display_links = ('type', )


admin.site.register(Car, CarAdmin)
admin.site.register(CarDBStatistics, CarDBStatisticsAdmin)
