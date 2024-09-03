from django.urls import path
from .views import HomeView, CategoriesView, EntreeListView, SoupStewChiliListView, DessertListView, RecipeDetailView, HomeView, CategoriesView, EntreeListView, SoupStewChiliListView, DessertListView,EntreeCreateView, DessertCreateView, SoupStewChiliCreateView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('categories/', CategoriesView.as_view(), name='categories'),
    path('entrees/', EntreeListView.as_view(), name='entrees'),
    path('entrees/new/', EntreeCreateView.as_view(), name='entree-create'),
    path('soups_stews_chilis/', SoupStewChiliListView.as_view(), name='soups_stews_chilis'),
    path('soups_stews_chilis/new/', SoupStewChiliCreateView.as_view(), name='soup-create'),
    path('desserts/', DessertListView.as_view(), name='desserts'),
    path('desserts/new/', DessertCreateView.as_view(), name='dessert-create'),
    path('recipe/<int:recipe_id>/<str:category>/', RecipeDetailView.as_view(), name='recipe_detail'),
]
