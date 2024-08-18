from django.db import models

# Create your models here.
from django.db import models

class Recipe(models.Model):
    CATEGORY_CHOICES = [
        ('entrees', 'Entrees'),
        ('desserts', 'Desserts'),
        ('soups_stews_chilis', 'Soups, Stews and Chilis'),
    ]

    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)  # Changed to a text field
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)

    def __str__(self):
        return self.title

class Ingredient(models.Model):
    QUANTITY_UNIT_CHOICES = [
        ('g', 'grams'),
        ('kg', 'kilograms'),
        ('ml', 'milliliters'),
        ('l', 'liters'),
        ('cup', 'cup'),
        ('tbsp', 'tablespoon'),
        ('tsp', 'teaspoon'),
        ('oz', 'ounces'),
        ('lb', 'pounds'),
        ('piece', 'piece'),
        ('can', 'can'),
        ('jar', 'jar'),
        ('package', 'package'),
        ('bunch', 'bunch'),
        ('pinch', 'pinch'),
        ('dash', 'dash'),
        ('to taste', 'to taste'),
        
    ]

    recipe = models.ForeignKey(Recipe, related_name='ingredients', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    quantity = models.DecimalField(max_digits=5, decimal_places=2)
    unit = models.CharField(max_length=20, choices=QUANTITY_UNIT_CHOICES)

    def __str__(self):
        return f"{self.quantity} {self.get_unit_display()} of {self.name}"

class Instruction(models.Model):
    recipe = models.ForeignKey(Recipe, related_name='instructions', on_delete=models.CASCADE)
    step_number = models.PositiveIntegerField()
    description = models.TextField()

    class Meta:
        ordering = ['step_number']

    def __str__(self):
        return f"Step {self.step_number}: {self.description}"

class Entree(Recipe):
    MAIN_CHOICES = [
        ('Chicken', 'Chicken'),
        ('Beef', 'Beef'),
        ('Pork', 'Pork'),
        ('Fish', 'Fish'),
        ('Shrimp', 'Shrimp'),
        ('Vegetarian', 'Vegetarian'),
    ]
    main_feature = models.CharField(max_length=50, choices=MAIN_CHOICES)

class Dessert(Recipe):
    DESSERT_TYPE_CHOICES = [
        ('Cake', 'Cake'),
        ('Pie', 'Pie'),
        ('Cookies', 'Cookies'),
        ('Other', 'Other'),
    ]
    dessert_type = models.CharField(max_length=50, choices=DESSERT_TYPE_CHOICES)

class SoupStewChili(Recipe):
    SOUP_STEW_CHILI_TYPE_CHOICES = [
        ('Bean', 'Bean'),
        ('Bisque', 'Bisque'),
        ('Chicken', 'Chicken'),
        ('Beef', 'Beef'),
        ('Noodle', 'Noodle'),
        ('Vegetable', 'Vegetable'),
        ('Seafood', 'Seafood'),
    ]
    soup_stew_chili_types = models.ManyToManyField('SoupStewChiliType')

class SoupStewChiliType(models.Model):
    type_name = models.CharField(max_length=50, choices=SoupStewChili.SOUP_STEW_CHILI_TYPE_CHOICES)

    def __str__(self):
        return self.type_name

'''
Ingredient.objects.create(recipe=recipe, name="Sugar", quantity=1.5, unit="cup")
Ingredient.objects.create(recipe=recipe, name="Butter", quantity=200, unit="g")
'''

'''
# Create a new Entree recipe
entree = Entree.objects.create(
    title="Grilled Chicken",
    author="Chef John",
    main_feature="Chicken"
)

# Add ingredients with quantity and unit
Ingredient.objects.create(recipe=entree, name="Chicken breast", quantity=2, unit="piece")
Ingredient.objects.create(recipe=entree, name="Olive oil", quantity=2, unit="tbsp")
Ingredient.objects.create(recipe=entree, name="Salt", quantity=1, unit="tsp")

# Add instructions
Instruction.objects.create(recipe=entree, step_number=1, description="Marinate the chicken with olive oil and salt.")
Instruction.objects.create(recipe=entree, step_number=2, description="Grill the chicken on medium heat for 6-7 minutes on each side.")
'''
