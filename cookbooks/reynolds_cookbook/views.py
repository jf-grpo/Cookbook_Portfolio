#views.py
from django.http import Http404
from django.views.generic import TemplateView, ListView, DetailView
from django.shortcuts import get_object_or_404
from .models import Entree, Dessert, SoupStewChili, Recipe

from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import EntreeForm, DessertForm, SoupStewChiliForm

# Home View
class HomeView(TemplateView):
    template_name = 'reynolds_cookbook/home.html'

# Categories View
class CategoriesView(TemplateView):
    template_name = 'reynolds_cookbook/categories.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['entrees'] = Entree.objects.all()[:2]
        context['desserts'] = Dessert.objects.all()[:2]
        context['soups_stews_chilis'] = SoupStewChili.objects.all()[:2]
        return context

# Entrees View
class EntreeListView(ListView):
    model = Entree
    template_name = 'reynolds_cookbook/entrees.html'
    context_object_name = 'entrees'

    def get_queryset(self):
        filter_main = self.request.GET.get('filter', None)
        if filter_main:
            return Entree.objects.filter(main_feature=filter_main)
        return Entree.objects.all() # Default to all Entrees
        # return Entree.objects.order_by('?')[:5]  # Default to 5 random Entrees

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['main_choices'] = Entree.MAIN_CHOICES
        return context

# Soups Stews Chilis View
class SoupStewChiliListView(ListView):
    model = SoupStewChili
    template_name = 'reynolds_cookbook/soups_stews_chilis.html'
    context_object_name = 'soups_stews_chilis'

    def get_queryset(self):
        filter_type = self.request.GET.get('filter', None)
        if filter_type:
            return SoupStewChili.objects.filter(soup_type=filter_type)
        return SoupStewChili.objects.all() # Default to all recipes
        # return SoupStewChili.objects.order_by('?')[:5]  # Default to 5 random recipes

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['soup_types'] = SoupStewChili.SOUP_TYPE_CHOICES
        return context

# Desserts View
class DessertListView(ListView):
    model = Dessert
    template_name = 'reynolds_cookbook/desserts.html'
    context_object_name = 'desserts'

    def get_queryset(self):
        filter_type = self.request.GET.get('filter', None)
        if filter_type:
            return Dessert.objects.filter(dessert_type=filter_type)
        return Dessert.objects.all() # Default to all Desserts
        # return Dessert.objects.order_by('?')[:5]  # Default to 5 random desserts

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['dessert_types'] = Dessert.DESSERT_TYPE_CHOICES
        return context

# Recipe Detail View
class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'reynolds_cookbook/recipe_detail.html'
    context_object_name = 'recipe'

    def get_object(self, queryset=None):
        recipe_id = self.kwargs.get('recipe_id')
        category = self.kwargs.get('category')

        # Determine the correct model based on category
        if category == 'entrees':
            return Entree.objects.get(pk=recipe_id)
        elif category == 'desserts':
            return Dessert.objects.get(pk=recipe_id)
        elif category == 'soups_stews_chilis':
            return SoupStewChili.objects.get(pk=recipe_id)
        else:
            raise Http404("Recipe not found")
        


# Entree Create View
class EntreeCreateView(CreateView):
    model = Entree
    form_class = EntreeForm
    template_name = 'reynolds_cookbook/entree_form.html'
    success_url = reverse_lazy('entrees')  # Redirect to the entree list view after form submission

# Dessert Create View
class DessertCreateView(CreateView):
    model = Dessert
    form_class = DessertForm
    template_name = 'reynolds_cookbook/dessert_form.html'
    success_url = reverse_lazy('desserts')  # Redirect to the dessert list view after form submission

# Soup Stew Chili Create View
class SoupStewChiliCreateView(CreateView):
    model = SoupStewChili
    form_class = SoupStewChiliForm
    template_name = 'reynolds_cookbook/soup_form.html'
    success_url = reverse_lazy('soups_stews_chilis')  # Redirect to the soup list view after form submission
