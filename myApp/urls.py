from myApp.views import mana, sec, news
from django.urls import path
from myApp import views


urlpatterns = [
    path('', views.mana, name = 'home'),
    #path('left/', views.sec, name = 'left'),
    path('left/<str:pk>/', views.sec, name = 'rooms'),
    # path('<str:pk>', views.show, name = 'show'),
    path('tested/<str:pk>/', views.news, name = 'tested'),
   # path('home/', views.home, name = 'home'),
    path("createroom/", views.createRoom, name='create_room')
]
