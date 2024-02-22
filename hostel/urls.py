# from django import views
from . import views
from django.urls import path

urlpatterns = [
    path('',views.home,name="home"),
    path('login/',views.login_page,name="login"),
    path('logout/',views.logout_page,name="logout"),
    path('Register/',views.Register_page,name="Register"),
    path('attendance/',views.attendance,name="attendance"),
    path('fee/',views.fee,name="fee"),
    path('review/',views.review,name="review"),
    path('room/',views.room,name="room"),
    path('complaint',views.complaint,name="complaint"),
]