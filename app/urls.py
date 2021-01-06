from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('', views.home, name='home'),
   #path('quiz/',views.quiz,name='quiz'),
   #path('',views.home,name='home'),
   
]