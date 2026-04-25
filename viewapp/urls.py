from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('football', views.football),
    path('football/', views.football),
    path('hockey', views.hockey),
    path('hockey/', views.hockey),
    path('basketball', views.basketball),
    path('basketball/', views.basketball),
]
