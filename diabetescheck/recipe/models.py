from django.db import models
from journal.models import Person


CATEGORY_OPTIONS = (
    ('carbohydrates', 'Carbohydrate'),
    ('proteins', 'Protein'),
    ('alcohol', 'Alcohol'),
    ('fats', 'Fats and Oils'),
    ('vitamins', 'Vitamin'),
    ('cholestrols', 'Cholestrol'),
    ('fiber', 'Fiber'),
    ('minerals', 'Mineral')
)


class Recipe(models.Model):
    """Available recipes."""

    person = models.ForeignKey(Person)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)
    ingredients = models.ManyToManyField(
        'FoodItem', through='RecipeFoodItem', related_name='foodItem_recipes',)
    instructions = models.TextField()
    prep_time = models.DurationField()
    serving = models.IntegerField()

    def __str__(self):
        """String representation of Recipe."""
        return self.name

    @property
    def nutrition_details_per_serving(self):
        """Return total calories divided by no of servings."""
        pass

    @property
    def ingredients_list(self):
        """Get the food item objects related to a particular recipe."""
        return self.ingredients.select_related()


class FoodItem(models.Model):
    """A distinguishable, simplest food item/ingredient."""

    name = models.CharField(max_length=255)
    nutritional_value = models.ManyToManyField(
        'FoodCategory', through='NutritionalValue')
    description = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        """Return a string representation of the FoodItem."""
        return self.name

    # @property
    # def calories(self):
    #     """Sum total of calories per consumed FoodItem."""
    #     units_consumed = self.amount / 100
    #     from pdb import set_trace
    #     set_trace()
    #     return self.fooditem_nutrients__calories_in_100g() * units_consumed


class RecipeFoodItem(models.Model):
    """A through table for ingredients manytomany field in Recipe model."""

    recipe = models.ForeignKey(Recipe, related_name='recipe_fooditem')
    food_item = models.ForeignKey(FoodItem, related_name='constituent_recipe')


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
    # quantity of FoodItem consumed in grams
    amount = models.FloatField()
    measurement_unit = models.CharField(max_length=255)
    quantity_per_unit = models.FloatField()

    @property
    def calories_in_units_consumed(self):
        """Return calories contributed by a given nutrient in a food_item."""
        total_consumption = self.amount * self.quantity_per_unit
        return self.category.caloric_value_per_gram * total_consumption

    def __str__(self):
        """String representation of NutritionalValue class."""
        return "food_item:{0}, category:{1}".format(
            self.food_item.name, self.category.category)
