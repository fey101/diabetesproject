from django.db import models
from django.conf import settings

OPTIONS = (
    ('carbohydrates', 'Carbohydrates'),
    ('proteins', 'Proteins'),
    ('alcohol', 'Alcohol'),
    ('fats', 'Fats and Oils')
)


CALORIC_CONSTANTS = {
    'proteins': 4,
    'carbohydrates': 4,
    'alcohol': 7,
    'fats': 9
}


class Recipe(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    name = models.CharField(max_length=255)
    ingredients = models.ManyToManyField(
        'FoodItem', related_name='FoodItem_recipes')
    instructions = models.TextField()
    prep_time = models.DurationField()
    serving = models.IntegerField()

    def __str__(self):
        return self.name


class FoodItem(models.Model):
    users = models.ManyToManyField(settings.AUTH_USER_MODEL)
    name = models.CharField(max_length=255)
    category = models.ManyToManyField(
        'FoodCategory', through='FoodItemCategory')

    def __str__(self):
        return self.name
    # carbohydrates = models.FloatField()
    # vitamins = models.FloatField()
    # proteins = models.FloatField()
    # cholestrol = models.FloatField()
    # oils = models.FloatField()
    # fats = models.FloatField()
    # alcohol = models.FloatField()
    # sodium = models.FloatField()

    # @property
    # def calories(self):
    #     from_proteins = self.proteins * CALORIC_CONSTANTS['proteins']
    #     from_carbs = self.carbohydrates * CALORIC_CONSTANTS['carbohydrates']
    #     from_fats = self.fats * CALORIC_CONSTANTS['fats']
    #     from_alcohol = self.alcohol * CALORIC_CONSTANTS['alcohol']

    #     return from_proteins + from_carbs + from_fats + from_alcohol


class FoodCategory(models.Model):
    category = models.CharField(max_length=25, choices=OPTIONS)
    caloric_value_per_gram = models.FloatField()

    def __str__(self):
        return self.category


class FoodItemCategory(models.Model):
    food_item = models.ForeignKey('FoodItem')
    category = models.ForeignKey('FoodCategory')
