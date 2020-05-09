from django.conf.urls import url
from django.urls import path
from turtle_words import views

urlpatterns = [
    path('', views.index, name='index'),
    path('brand', views.turtle_brand, name='brand'),
    path('turtle_brand_search', views.turtle_brand_search, name='search'),
    path('turtle_brand_signup', views.turtle_brand_signup, name='signup')
]
