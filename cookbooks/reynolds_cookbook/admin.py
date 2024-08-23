from django.contrib import admin
from .models import Recipe, Ingredient, Instruction, Entree, Dessert, SoupStewChili

class IngredientInline(admin.TabularInline):
    model = Ingredient
    extra = 1  # How many extra blank fields to show

class InstructionInline(admin.TabularInline):
    model = Instruction
    extra = 1  # How many extra blank fields to show

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category')
    search_fields = ('title', 'author', 'category')
    list_filter = ('category',)
    inlines = [IngredientInline, InstructionInline]

@admin.register(Entree)
class EntreeAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'main_feature')
    search_fields = ('title', 'author', 'main_feature')
    list_filter = ('main_feature',)
    inlines = [IngredientInline, InstructionInline]

@admin.register(Dessert)
class DessertAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'dessert_type')
    search_fields = ('title', 'author', 'dessert_type')
    list_filter = ('dessert_type',)
    inlines = [IngredientInline, InstructionInline]

@admin.register(SoupStewChili)
class SoupStewChiliAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'soup_type')
    search_fields = ('title', 'author', 'soup_type')
    list_filter = ('soup_type',)
    inlines = [IngredientInline, InstructionInline]
