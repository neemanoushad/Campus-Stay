"""Hostel_Management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path

from Hostel import hostel_urls,guest_urls
from Hostel.views import IndexView,LoginView,Guest_reg,Hostel_reg
from Hostel_Management import settings

urlpatterns = [
    path('',IndexView.as_view()),
    path('user_register',Guest_reg.as_view()),
    path('Hostel_reg',Hostel_reg.as_view()),
    path('login',LoginView.as_view()),
    # path('admin/',admin_urls.urls()),
    path('hostel/',hostel_urls.urls()),
    path('student/',guest_urls.urls()),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


