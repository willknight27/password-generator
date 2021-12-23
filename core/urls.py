from django.urls import path
from .views import about, home, password

urlpatterns = [
    path('',home,name="home"),
    path('about/',about,name="about"),
    path('password/',password, name="password"),

]
