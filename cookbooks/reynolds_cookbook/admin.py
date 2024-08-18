from django.contrib import admin
from .models import Entree, Dessert, SoupStewChili, Ingredient, Instruction

# admin.site.unregister(Recipe)

class IngredientInline(admin.TabularInline):
    model = Ingredient
    extra = 1

class InstructionInline(admin.TabularInline):
    model = Instruction
    extra = 1

# @admin.register(Recipe)
# class RecipeAdmin(admin.ModelAdmin):
#     list_display = ('title', 'author', 'category')  # Display author as a text field
#     search_fields = ('title', 'author')  # Searchable by author name
#     list_filter = ('category',)  # Adds a filter sidebar for categories

@admin.register(Entree)
class EntreeAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'main_feature')
    inlines = [IngredientInline, InstructionInline]

@admin.register(Dessert)
class DessertAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'dessert_type')
    inlines = [IngredientInline, InstructionInline]

@admin.register(SoupStewChili)
class SoupStewChiliAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')
    inlines = [IngredientInline, InstructionInline]

# @admin.register(Ingredient)
# class IngredientAdmin(admin.ModelAdmin):
#     list_display = ('name', 'quantity', 'unit', 'recipe')

# @admin.register(Instruction)
# class InstructionAdmin(admin.ModelAdmin):
#     list_display = ('step_number', 'description', 'recipe')
