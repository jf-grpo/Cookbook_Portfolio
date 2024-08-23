from django.db import models

# Create your models here.

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
    SOUP_TYPE_CHOICES = [
        ('Chili', 'Chili'),
        ('Soup', 'Soup'),
        ('Stew', 'Stew'),
    ]
    soup_type = models.CharField(max_length=50, choices=SOUP_TYPE_CHOICES, default='Soup')