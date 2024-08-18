from django.views.generic import TemplateView, ListView, DetailView
from django.shortcuts import get_object_or_404
from .models import Entree, Dessert, SoupStewChili

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
    template_name = 'entrees.html'
    context_object_name = 'entrees'

    def get_queryset(self):
        filter_main = self.request.GET.get('filter', None)
        if filter_main:
            return Entree.objects.filter(main_feature=filter_main)
        return Entree.objects.order_by('?')[:5]  # Default to 5 random Entrees

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['main_choices'] = Entree.MAIN_CHOICES
        return context

# Soups Stews Chilis View
class SoupStewChiliListView(ListView):
    model = SoupStewChili
    template_name = 'soups_stews_chilis.html'
    context_object_name = 'soups_stews_chilis'

    def get_queryset(self):
        filter_type = self.request.GET.get('filter', None)
        if filter_type:
            return SoupStewChili.objects.filter(soup_stew_chili_types__type_name=filter_type)
        return SoupStewChili.objects.order_by('?')[:5]  # Default to 5 random recipes

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['types'] = SoupStewChili.SOUP_STEW_CHILI_TYPE_CHOICES
        return context

# Desserts View
class DessertListView(ListView):
    model = Dessert
    template_name = 'desserts.html'
    context_object_name = 'desserts'

    def get_queryset(self):
        filter_type = self.request.GET.get('filter', None)
        if filter_type:
            return Dessert.objects.filter(dessert_type=filter_type)
        return Dessert.objects.order_by('?')[:5]  # Default to 5 random desserts

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['dessert_types'] = Dessert.DESSERT_TYPE_CHOICES
        return context

# Recipe Detail View
class RecipeDetailView(DetailView):
    template_name = 'recipe_detail.html'

    def get_object(self):
        category = self.kwargs.get('category')
        recipe_id = self.kwargs.get('recipe_id')

        if category == 'entrees':
            return get_object_or_404(Entree, id=recipe_id)
        elif category == 'soups_stews_chilis':
            return get_object_or_404(SoupStewChili, id=recipe_id)
        elif category == 'desserts':
            return get_object_or_404(Dessert, id=recipe_id)
