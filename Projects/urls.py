from django.contrib import admin
from django.urls import path

from Main.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
]
