from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='home', kwargs={'name':'Бахтияров Согдияр Бахтиярович','age':'16','interests':'какие то там допустим интересы, к примеру программирование'}),
    re_path('about', views.about, name='about', kwargs={'I_from':'kyrgyzstan','performance':'4.12','study':'yes'}),
    re_path('contacts', views.contacts,name='contacts', kwargs={'GitHub':'sogdiyar008','Telegramm':'Sogdiyar008','contact':'+7 950 321 98 69', 'contact1':'+996 706 79 11 25'}),
]