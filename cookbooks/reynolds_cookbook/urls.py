from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('recipes/', views.recipes, name='recipes'),
    path('categories/', views.categories, name='categories'),
]