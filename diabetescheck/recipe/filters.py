import django_filters

from .models import (
    Recipe,
    Ingredients,
    RecipeIngredient,
    Nutrients,
    RecipeNutrients
)


class RecipeFilter(django_filters.FilterSet):
    class Meta:
        model = Recipe


class IngredientsFilter(django_filters.FilterSet):
    class Meta:
        model = Ingredients


class RecipeIngredientFilter(django_filters.FilterSet):
    class Meta:
        model = RecipeIngredient


class NutrientsFilter(django_filters.FilterSet):
    class Meta:
        model = Nutrients


class RecipeNutrientsFilter(django_filters.FilterSet):
    class Meta:
        model = RecipeNutrients
