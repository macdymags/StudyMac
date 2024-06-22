from django.urls import path
from. import views

urlpatterns = [
    path('', views.index, name='index'),
    path('shipment/<int:pk>/', views.shipment_detail, name='shipment_detail'),
    path('transit/<int:pk>/', views.transit_detail, name='transit_detail'),
]