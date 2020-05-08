"""netflix URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from views import *





urlpatterns = [
    path('adminRegisteration', adminRegisteration),
    path('adminLogin', adminLogin),
    path('adminlogout', adminlogout),
    path('adminview', adminview),
    path('alladmin', alladmin),
    path('adminChangePassword', adminChangePassword),
    path('adminUpdate', adminUpdate),
    path('adminDelete', adminDelete),

    path('addgenre',addgenre),
    path('viewgenre', viewgenre),
    path('deletegenre',deletegenre),

    path('addcategory',addcategory),
    path('viewcategory', viewcategory),
    path('deletecategory',deletecategory),
    path('updateCategorySave',updateCategorySave),

    path('addvideos',addvideos),
    path('deletevideos',deletevideos),
    path('updatevideos',updatevideos),
    path('viewMovies', viewMovies),

    path('addEpisodes',addEpisodes),
    path('viewEpisode',viewEpisode),
    path('deleteEpisode',deleteEpisode),
    path('updateEpisode',updateEpisode),

    path('',view),
    path('login',clientlogin),
    path('browse',browseview),
    path('browsedata',browsedata),
    path('detail',detail),
    path('paymentoffer',paymentoffer),

    path('clientlogin',clientlogin),
    path('clientRegistration',clientRegistration),
    path('changepassword',clientChangePassword),
    path('logout',clientlogout),
    path('forgetpassword',forgetpassword),
    path('forgetpage',forgetpage),
    path('otpchangepassword',otpchangepassword),

    path('person1',person1),
    path('person2',person2),
    path('person4',person4),

    path('paymentBill',paymentBill),
    path('thanksyou',thanksyou),
    path('failpayment',failpayment),
    path('subscribe',subscribe),
    path('screendisplay',screendisplay),
    path('allshows',allshows),
    path('searchlist',searchlist),
    path('4o4page',http4o4page)

]
