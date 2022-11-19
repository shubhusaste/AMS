"""EMS URL Configuration

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
from django.urls import path,include
from . import views

urlpatterns = [
    path ('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('register/',views.register,name='register'),
    path('adminlogin/',views.adminlogin,name='adminlogin'),
    path('userlogin/',views.userlogin,name='userlogin'),
    path('userhome/',views.userhome,name='userhome'),
    path('adminhome/',views.adminhome,name='adminhome'),
    path('addalumni/',views.addalumni,name='addalumni'),
    path('viewalumni/',views.viewalumni,name='viewalumni'),
    path('gallary/',views.gallary,name='gallary'),
    path('addgallary/',views.addgallary,name='addgallary'),

    path('logout/',views.logout,name='logout'),
    path('admin_updateprofile/<int:id>',views.admin_updateprofile,name='admin_updateprofile'),
    path('admin_deletealumni/<int:id>',views.admin_deletealumni,name='admin_deletealumni'),
    path('updateyourprofile/',views.updateyourprofile,name='updateyourprofile'),
    path('changeuserpassword/',views.changeuserpassword,name='changeuserpassword'),
    path('branch_Alumni/',views.branch_Alumni,name='branch_Alumni'),



]
