from ecomapp import views
from django.urls import path

urlpatterns = [
    path('', views.getRoutes,name='Routes'),
    path('products/', views.getProducts,name='data'),
    path('products/<str:pk>', views.getProduct,name='data')
]