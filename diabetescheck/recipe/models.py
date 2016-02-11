from django.db import models
from journal.models import Person


CATEGORY_OPTIONS = (
    ('carbohydrates', 'Carbohydrate'),
    ('proteins', 'Protein'),
    ('alcohol', 'Alcohol'),
    ('fats', 'Fats and Oils'),
    ('vitamins', 'Vitamin'),
    ('cholestrols', 'Cholestrol'),
    ('minerals', 'Mineral')
)


CALORIC_CONSTANTS = {
    'proteins': 4,
    'carbohydrates': 4,
    'alcohol': 7,
    'fats': 9
}


class Recipe(models.Model):
    """Available recipes."""

    user = models.ForeignKey(Person)
    name = models.CharField(max_length=255)
    ingredients = models.ManyToManyField(
        'FoodItem', related_name='FoodItem_recipes')
    instructions = models.TextField()
    prep_time = models.DurationField()
    serving = models.IntegerField()

    def __str__(self):
        """String representation of Recipe."""
        return self.name


class FoodItem(models.Model):
    """A distinguishable, simplest food item/ingredient."""

    name = models.CharField(max_length=255)
    nutritional_value = models.ManyToManyField(
        'FoodCategory', through='NutritionalValue')
    # quantity of FoodItem consumed in grams
    amount = models.FloatField()

    def __str__(self):
        """Return a string representation of the FoodItem."""
        return self.name

    @property
    def calories(self):
        """Sum total of calories per consumed FoodItem."""
        units_consumed = self.amount / 100
        return self.fooditem_nutrients.calories_in_100g() * units_consumed


class FoodCategory(models.Model):
    """Food categorised into proteins, carbohydrates, vitamins, e.t.c."""

    category = models.CharField(max_length=25, choices=CATEGORY_OPTIONS)
    caloric_value_per_gram = models.FloatField()

    def __str__(self):
        """Return category as string representation of FoodCategory class."""
        return self.category


class NutritionalValue(models.Model):
    """
    Nutrients in a food_item.

    Also a through table between FoodItem and FoodCategory models.
    This model has pre-defined constants for example in 100g of milk there
    is 9g of protein and 12g of carbohydrates.
    """

    food_item = models.ForeignKey(
        'FoodItem', related_name="fooditem_nutrients")
    category = models.ForeignKey(
        'FoodCategory', related_name="category_nutrients")
    quantity_per_100g = models.FloatField()

    def calories_in_100g(self):
        """Return calories contributed by a given nutrient in a food_item."""
        return self.category.caloric_value_per_gram * self.quantity_per_100g
