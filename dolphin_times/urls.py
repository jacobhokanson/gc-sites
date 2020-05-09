from django.conf.urls import url
from django.urls import path
from dolphin_times import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('details', views.details, name = 'details'),
]
