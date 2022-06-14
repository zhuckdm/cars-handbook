from django.contrib import admin
from django.urls import path, include

from carshandbook.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('carshandbook.urls')),
]
