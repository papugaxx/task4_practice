from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello_en),
    path('fr', views.hello_fr),
    path('fr/', views.hello_fr),
    path('de', views.hello_de),
    path('de/', views.hello_de),
    path('es', views.hello_es),
    path('es/', views.hello_es),
]
