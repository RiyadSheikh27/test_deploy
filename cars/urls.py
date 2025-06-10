from django.urls import path
from . import views  # Ensure this line is present to import views

urlpatterns = [
    path('', views.car_management, name='car_management'),  # Frontend URL
    path('api/cars/', views.CarsViewset.as_view(), name='cars_api'),  # API for car data
    path('api/cars/<int:id>', views.CarsViewset.as_view(), name='car_detail_api'),  # API for single car
]
