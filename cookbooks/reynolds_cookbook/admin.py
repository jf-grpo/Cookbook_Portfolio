from django.contrib import admin
from .models import Entree, Dessert, SoupStewChili, Ingredient, Instruction

# Inline classes to display Ingredients and Instructions within the Recipe admin pages
class IngredientInline(admin.TabularInline):
    model = Ingredient
    extra = 1  # Defines how many empty slots are shown to add new ingredients

class InstructionInline(admin.TabularInline):
    model = Instruction
    extra = 1  # Defines how many empty slots are shown to add new instructions

# Admin class for Entree model
@admin.register(Entree)
class EntreeAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'main_feature')  # Display these fields in the admin list view
    inlines = [IngredientInline, InstructionInline]  # Add Ingredients and Instructions in the Entree admin view

# Admin class for Dessert model
@admin.register(Dessert)
class DessertAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'dessert_type')
    inlines = [IngredientInline, InstructionInline]

# Admin class for SoupStewChili model
@admin.register(SoupStewChili)
class SoupStewChiliAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')  # Display title and author in the list view
    inlines = [IngredientInline, InstructionInline]

# Register Ingredient and Instruction models separately, if needed for direct management
@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name', 'quantity', 'unit', 'recipe')

@admin.register(Instruction)
class InstructionAdmin(admin.ModelAdmin):
    list_display = ('step_number', 'description', 'recipe')
