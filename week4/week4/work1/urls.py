from django.urls import path

from work1 import views

urlpatterns = [
    path('', views.home, name="home"),
    path('save_survey', views.save_survey, name="save"),
    path('show_result/<int:survey_idx>', views.show_result, name="result"),
    
]