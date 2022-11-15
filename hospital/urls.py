# from django.conf.urls.defaults import *
from . import views
from django.contrib import admin
from django.urls import path, include


urlpatterns = (
    path('patient_list/', views.patient_list),
    path('', views.home),
    path('beds/', views.add_beds),
    path('rem_beds/', views.rem_beds),
    # path('del_beds/', views.del_bed),
    path('del_beds/<int:id>', views.del_bed),
)