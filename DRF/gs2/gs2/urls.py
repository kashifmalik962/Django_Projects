from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('stuInfo/<int:pk>', views.StudentDetail),
    path('stuInfo/', views.StudentList),
    path('studata/', views.Student_data),
    path('studata/<int:pk>', views.Student_data)
]