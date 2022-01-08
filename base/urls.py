from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='Home'), # can take 3 parameters.
    path('room/', views.room, name='Room')

]