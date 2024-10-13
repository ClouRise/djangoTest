from django.urls import path
from . import views

urlpatterns = [
    path('', views.infomain),
    path('info/', views.definfo),
]
