from django.urls import path
from .views import HomeView, CategoriesView, EntreeListView, SoupStewChiliListView, DessertListView, RecipeDetailView, HomeView, CategoriesView, EntreeListView, SoupStewChiliListView, DessertListView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('categories/', CategoriesView.as_view(), name='categories'),
    path('entrees/', EntreeListView.as_view(), name='entrees'),
    path('soups_stews_chilis/', SoupStewChiliListView.as_view(),name='soups_stews_chilis'),
    path('desserts/', DessertListView.as_view(), name='desserts'),
    path('recipe/<int:recipe_id>/<str:category>/', RecipeDetailView.as_view(), name='recipe_detail'),
]
