from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home, name="home"),
    path('send',views.send,name="send"),
    path('goal',views.goal,name='goal'),
    path('play',views.play,name='play'),
    path('detail_1',views.detail_1,name='detail_1'),
    path('volunteer',views.volunteer,name='volunteer'),
    #path('delete/<int:pk>',views.delete,name='delete'),
    path('search',views.search, name='search'),
    path('detail_2',views.detail_2,name='detail_2'),
    path('detail_3',views.detail_3,name='detail_3'),
    path('detail_4',views.detail_4,name='detail_4'),
    path('detail_5',views.detail_5,name='detail_5'),
    path('detail_6',views.detail_6,name='detail_6'),
    path('detail_7',views.detail_7,name='detail_7'),
    path('detail_8',views.detail_8,name='detail_8'),
    path('detail_9',views.detail_9,name='detail_9'),
    path('detail_10',views.detail_10,name='detail_10'),
    path('detail_11',views.detail_11,name='detail_11'),
    path('detail_12',views.detail_12,name='detail_12'),
    path('detail_13',views.detail_13,name='detail_13'),
    path('detail_14',views.detail_14,name='detail_14'),
    path('detail_15',views.detail_15,name='detail_15'),
    path('detail_16',views.detail_16,name='detail_16'),
    path('detail_17',views.detail_17,name='detail_17'),
]