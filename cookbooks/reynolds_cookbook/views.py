from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

# Create your views here.
tempRecipes = [
    {"title": "Chicken Alfredo", "description": "A creamy pasta dish with chicken and broccoli."},
    {"title": "Spaghetti and Meatballs", "description": "A classic pasta dish with marinara sauce."},
    {"title": "Chicken Parmesan", "description": "Breaded chicken with marinara sauce and melted cheese."},
]

tempCategories = [
    {"name": "Entrees"},
    {"name": "Appetizers"},
    {"name": "Desserts"},
    {"name": "Soups, Stews, and Chili"},
    {"name": "Salads"},
]

tempMain = [
    {"Feature": "Chicken"},
    {"Feature": "Beef"},
    {"Feature": "Pork"},
    {"Feature": "Fish"},
    {"Feature": "Shrimp"},
    {"Feature": "Vegeterian"},
]

def home(request):
    return render(request, "reynolds_cookbook/home.html")

def recipes(request):
    context = {"tempRecipes": tempRecipes}
    return render(request, "reynolds_cookbook/recipes_list.html", context)
# class RecipesList(ListView):
#     model = RecipesList
#     template_name = "reynolds_cookbook/recipes_list.html"
def categories(request):
    context = {"tempCategories": tempCategories}
    return render(request, "reynolds_cookbook/categories_list.html", context)
# class CategoriesList(ListView):
#     model = CategoriesList
#     template_name = "reynolds_cookbook/categories_list.html"
# def main(request):
#     context = {"tempMain": tempMain}
#     return render(request, "reynolds_cookbook/main_list.html", context)