from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

# Create your views here.
tempRecipes = [
    {"title": "Chicken Alfredo", "description": "A creamy pasta dish with chicken and broccoli."},
    {"title": "Spaghetti and Meatballs", "description": "A classic pasta dish with marinara sauce."},
    {"title": "Chicken Parmesan", "description": "Breaded chicken with marinara sauce and melted cheese."},
]

def home(request):
    context = {"name": "Reynolds", 'tempRecipes': tempRecipes}
    return render(request, "reynolds_cookbook/home.html", context)

# class RecipesList(ListView):
#     model = RecipesList
#     template_name = "reynolds_cookbook/recipes_list.html"

# class CategoriesList(ListView):
#     model = CategoriesList
#     template_name = "reynolds_cookbook/categories_list.html"