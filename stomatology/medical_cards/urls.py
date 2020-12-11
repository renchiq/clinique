from django.urls import path
from . import views

urlpatterns = [
    path('<str:pk>/', views.medical_card_info),
    path('<str:pk>/records/', views.medical_card_records),
]