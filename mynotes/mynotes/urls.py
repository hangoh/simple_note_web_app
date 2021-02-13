"""mynotes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path,include
from main_app import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home_page,name='home'),
    path('login/',views.login_account,name='login'),
    path('register_account/',views.register_account,name='register'),
    path('logout_account',views.logout_account,name='logout'),
    path('notes/',include('notes.urls'))
]
