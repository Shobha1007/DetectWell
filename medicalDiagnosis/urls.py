from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.base, name = 'index'),
    path('heartdis',views.heartdis, name = 'heartdis'),
    path('diabetes',views.diabetes, name = 'diabetes'),
    path('parkinsons',views.parkinsons, name = 'parkinsons')

   
]