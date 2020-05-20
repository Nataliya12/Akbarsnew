from django.contrib import admin
from django.urls import path,include
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [

    path('', index),
    path('login/', login),
    path('page/', page, name='page'),
    path('sertification/<int:id>/', ser),
    path('reg_ok/', reg_ok),
    path('reg/', reg),
    path('logout/', LogoutView.as_view(template_name='mainpage.html')),
    path('newday/', newday),
    path('portal/', portal),
    path('portal/new1/', new1),
    path('portal/new2/', new2),
    path('portal/new3/', new3),
    path('portal/new4/', new4),
    path('portal/new5/', new5),
    path('portal/new6/', new6),
    path('portal/new7/', new7),
    path('portal/new8/', new8),
    path('portal/new9/', new9),
    path('portal/new10/', new10),
    path('portal/new11/', new11),
    path('portal/new12/', new12),
    path('portal/new13/', new13),
    path('portal/new14/', new14),
    path('portal/new15/', new15),
    path('portal/new16/', new16),
    path('portal/new17/', new17),
    path('portal/new18/', new18),
    path('portal/new19/', new19),
    path('lk/', lk, name='lk'),
    path('lk/red/', red),
    path('sertification/', sertification),
        ]