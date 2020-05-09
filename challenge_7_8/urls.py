from django.contrib import admin
from django.urls import path
from django.conf.urls import include

urlpatterns = [
    path('', include('dolphin_times.urls')), # autodirect localhost:8000 to the turtle index
    path('challenge_7/', include("turtle_words.urls")),
    path('challenge_8/', include("dolphin_times.urls")),
    path('admin/', admin.site.urls),
]
