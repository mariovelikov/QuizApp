from django.urls import path
from . import views

urlpatterns = [
    path('', views.LandingPage, name='landing page'),
    path('<int:pk>/', views.quiz_data, name='questions'),
    path('<int:pk>/result/', views.result, name='quiz result'),
    path('<int:pk>/saveans/', views.saveans, name='save answer'),
]
