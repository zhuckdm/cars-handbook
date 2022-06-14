from django.urls import path

from carshandbook.views import *


urlpatterns = [
    path('carlist/', CarAPIListView.as_view()),
    path('carlist/<int:pk>', CarAPIView.as_view()),
    path('cardbstatisticslist/', CarDBStatisticsAPIView.as_view()),
]
