from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('result', views.show_result, name="result"),
    path('save_survey/', views.save_survey, name="save_survey" )
]
