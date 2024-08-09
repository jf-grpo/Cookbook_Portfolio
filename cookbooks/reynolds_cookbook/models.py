from django.db import models

# Create your models here.
from django.db import models
from django.contrib.postgres.fields import JSONField

class Recipe(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    ingredients = JSONField(default=list)  # Stores a list of dictionaries for ingredients
    instructions = JSONField(default=list)  # Stores a list of steps

    class Meta:
        abstract = True  # Makes this an abstract base class

    def __str__(self):
        return self.title

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

    def __str__(self):
        return f"{self.title} - {self.main_feature}"

class Dessert(Recipe):
    DESSERT_TYPE_CHOICES = [
        ('Cake', 'Cake'),
        ('Pie', 'Pie'),
        ('Cookies', 'Cookies'),
        ('Other', 'Other'),
    ]
    dessert_type = models.CharField(max_length=50, choices=DESSERT_TYPE_CHOICES)

    def __str__(self):
        return f"{self.title} - {self.dessert_type}"

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

    def __str__(self):
        return self.title

class SoupStewChiliType(models.Model):
    type_name = models.CharField(max_length=50, choices=SoupStewChili.SOUP_STEW_CHILI_TYPE_CHOICES)

    def __str__(self):
        return self.type_name

'''Model Notes:
# Create an Entree recipe Example
entree_recipe = Entree.objects.create(
    title="Grilled Chicken",
    author="Chef John",
    main_feature="Chicken",
    ingredients=[
        {"name": "Chicken breast", "quantity": "2 pieces"},
        {"name": "Olive oil", "quantity": "2 tablespoons"},
        {"name": "Salt", "quantity": "1 teaspoon"}
    ],
    instructions=[
        "Marinate the chicken with olive oil and salt.",
        "Grill the chicken on medium heat for 6-7 minutes on each side."
    ]
)

# Create a Dessert recipe Example
dessert_recipe = Dessert.objects.create(
    title="Apple Pie",
    author="Baker Jane",
    dessert_type="Pie",
    ingredients=[
        {"name": "Apples", "quantity": "3"},
        {"name": "Sugar", "quantity": "1 cup"},
        {"name": "Flour", "quantity": "2 cups"}
    ],
    instructions=[
        "Preheat the oven to 375°F.",
        "Prepare the pie crust and fill with apple mixture.",
        "Bake for 45 minutes or until golden brown."
    ]
)
'''


