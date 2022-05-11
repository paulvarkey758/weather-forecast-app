from django.urls import path
from . import views
urlpatterns=[
    path('',views.mainfun,name="mainfun"),
    path('showweather',views.showweather,name="showweather"),
]