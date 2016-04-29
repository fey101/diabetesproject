from django.db import models


RECIPE_CATEGORY = (
    ('bf', 'Breakfast'),
    ('lunch', 'Lunch'),
    ('supper', 'Supper'),
    ('snack', "Snack")
)


class Recipe(models.Model):
    """Available recipes."""

    name = models.CharField(max_length=255)
    photo = models.TextField(blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    ingredients = models.ManyToManyField(
        'Ingredients', through='RecipeIngredient',
        related_name='ingredient_recipe',)
    instructions = models.TextField()
    prep_time = models.DurationField()
    nutrients = models.ManyToManyField(
        'Nutrients', through='RecipeNutrients', related_name='nutrient_recipe')
    serving = models.IntegerField()
    category = models.CharField(max_length=25, choices=RECIPE_CATEGORY)


class Ingredients(models.Model):
    """Recipe ingredients."""

    name = models.CharField(max_length=255)
    amount = models.CharField(max_length=10)
    unit_of_measure = models.CharField(
        max_length=60, null=True, blank=True)
    description = models.CharField(max_length=255)


class RecipeIngredient(models.Model):
    """A through table for recipe-ingredint ManyToMany relationship."""

    recipe = models.ForeignKey(Recipe)
    ingredient = models.ForeignKey(Ingredients)


class Nutrients(models.Model):
    """The nutritional value details of a recipe.

    Always start with "Calories" as first nutrient and have "Cholesterol"
    as 7th, in providing data for purposes of sync with frontend.
    TODO: model this object better to avoid order being important.
    """

    name = models.CharField(max_length=255)
    quantity = models.DecimalField(max_digits=8, decimal_places=2)
    unit = models.CharField(max_length=10)


class RecipeNutrients(models.Model):
    """A through table for Recipe-Nutrients ManyToMany relationship."""

    recipe = models.ForeignKey(Recipe)
    nutrient = models.ForeignKey(Nutrients)
