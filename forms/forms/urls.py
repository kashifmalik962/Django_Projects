from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.userLogin, name="user_login"),
    path("register/",views.register, name="register"),
    path("home/",views.home, name="home")
]