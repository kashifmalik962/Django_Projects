from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api import views

router = DefaultRouter()
router.register('studentapi',views.Student_data, basename='student')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('stuInfo/<int:pk>', views.StudentDetail),
    path('stuInfo/', views.StudentList),
    path('', views.Student_data.as_view()),
    path('<int:pk>', views.Student_data.as_view())
]