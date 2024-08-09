from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    #path('recipes/', views.RecipesList.as_view(), name='recipes'),
    #path('categories/', views.CategoriesList.as_view(), name='categories'),
]