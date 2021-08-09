"""AnyPlace URL Configuration

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
from django.urls import path
from Home import views

urlpatterns = [
    path('',views.index,name='index'),
    path('contact',views.contact,name='contact'),
    path('newc',views.newc,name='newcategory'),
    path('about',views.about,name='about'),
    path('search',views.search,name='search'),
    path('login',views.login,name='login'), 
    path('signup',views.signup,name='signup'),
    path('loginuser',views.loginuser,name='loginuser'), 
    path('logoutuser',views.logoutuser,name='logoutuser'), 
    path('categories',views.categories,name='categories'), 
    path('register',views.register,name='register'), 
    path('addbussiness',views.addBussiness,name='addbussiness'), 
    path('adv',views.adv,name='advocate'), 
    path('ast',views.ast,name='astrologer'),
    path('aut',views.aut,name='automobile'), 
    path('bkr',views.bkr,name='bakery'), 
    path('bnk',views.bnk,name='bank'), 
    path('books',views.books,name='books'), 
    path('bldr',views.bldr,name='builder'), 
    path('ca',views.ca,name='ca'), 
    path('carp',views.carp,name='carpentr'), 
    path('clth',views.clth,name='cloths'), 
    path('cmputr',views.cmputr,name='computer'), 
    path('ctring',views.ctring,name='catering'), 
    path('cr',views.cr,name='courier'), 
    path('dct',views.dct,name='doctor'), 
    path('drv',views.drv,name='driver'), 
    path('dry',views.dry,name='drycleaner'), 
    path('elect',views.elect,name='electrician'), 
    path('electr',views.electr,name='electronics'), 
    path('em',views.em,name='event management'), 
    path('ff',views.ff,name='fast food'), 
    path('fw',views.fw,name='footwear'), 
    path('fn',views.fn,name='furniture'), 
    path('ga',views.ga,name='gas agency'), 
    path('gs',views.gs,name='gift shop'), 
    path('gm',views.gm,name='gym'),
    path('hs',views.hs,name='hair saloon'),
    path('hotel',views.hotel,name='hotel'),
    path('js',views.js,name='jwellery'),
    path('k&g',views.k_g,name='kirana general'),
    path('lb',views.lb,name='labour'),
    path('mdc',views.mdc,name='medical'),
    path('md',views.md,name='milk'),
    path('nws',views.nws,name='news'),
    path('opt',views.opt,name='optical'),
    path('pp',views.pp,name='petrol pump'),
    path('ps',views.ps,name='p studio'),
    path('pl',views.pl,name='plumber'),
    path('pd',views.pd,name='property'),
    path('rst',views.rst,name='restaurent'),
    path('sch',views.sch,name='school'),
    path('tl',views.tl,name='tailor'),
    path('thd',views.thd,name='tent'),
    path('tf',views.tf,name='tifin'),
    path('trn',views.trn,name='transport'),
    path('row',views.row,name='RO water'),
    

]