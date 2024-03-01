# from django import views
from . import views
from django.urls import path

urlpatterns = [
    path('',views.home,name="home"),
    path('profile/', views.profile, name='profile'),
    path('login/',views.login_page,name="login"),
    path('logout/',views.logout_page,name="logout"),
    path('register/',views.Register_page,name="register"),
    path('review/',views.review,name="review"),
]