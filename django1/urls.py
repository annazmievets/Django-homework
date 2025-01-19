"""
URL configuration for django1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from first.views import index_page, time_page, calc_page, expression_page, history_page, delete_page, clear_page, new_page, str2words_page, str_history_page, login_page, logout_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_page, name='index'),
    path('time/', time_page, name='time'),
    path('calc/', calc_page, name='calc'),
    path('expression/', expression_page, name='expression'),
    path('history/', history_page, name='history'),
    path('delete/', delete_page, name='delete'),
    path('clear/', clear_page, name='clear'),
    path('new/', new_page, name='new'),
    path('str2words/', str2words_page, name='str2words'),
    path('str_history/', str_history_page, name='str_history'),
    path('login/', login_page, name='login'),
    path('logout/', logout_page, name='logout'),
]
