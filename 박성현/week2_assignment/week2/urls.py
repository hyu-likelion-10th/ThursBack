"""week2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
import calculator.views
import wordcount.views

urlpatterns = [
    path('admin/', admin.site.urls),
    # calculator 앱과 연결해주세요.
    path('main',calculator.views.main, name='main'),
    path('calculator',calculator.views.calculator, name='calculator'),
    path('wordcount', wordcount.views.wordcount, name="wordcount"),
    path('home', wordcount.views.home, name="home")
]
