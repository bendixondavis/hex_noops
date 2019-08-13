from django.urls import path
from . import views

urlpatterns = [
    path('', views.my_color, name='my_color'),
]
