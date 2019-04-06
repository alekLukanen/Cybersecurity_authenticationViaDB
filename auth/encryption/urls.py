from django.urls import path, include
from . import views

urlpatterns = [
        path('public-key', views.public_key),
        path('date-time', views.current_datetime)
]
