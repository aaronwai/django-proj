from django.urls import path
from . import views
# set the / api, as variable=index to callback function
# /accounts/   all the accounts api
# setup all the possible accounts route

urlpatterns = [
    path('login', views.login, name="login"),
    path('register', views.register, name="register"),
    path('logout', views.logout, name="logout"),
    path('dashboard', views.dashboard, name="dashboard")
]
