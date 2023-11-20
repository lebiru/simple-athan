from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_prayer_times, name='get_prayer_times'),
    path('get-times', views.get_prayer_times, name='get_times_by_geo'),
]

