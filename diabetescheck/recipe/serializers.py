from rest_framework import serializers


from .models import (
    Recipe,
    Ingredients,
    RecipeIngredient,
    Nutrients,
    RecipeNutrients,
)


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredients


class NutrientsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Nutrients


class RecipeSerializer(serializers.ModelSerializer):
    ingredients_list = IngredientSerializer(
        many=True, read_only=True, source='ingredients')
    nutrients_list = NutrientsSerializer(
        many=True, read_only=True, source='nutrients')

    class Meta:
        model = Recipe
        fields = ("id", "name", "category", "description", "instructions",
                  "prep_time", "serving", "ingredients", "ingredients_list",
                  "nutrients", "nutrients_list")


class RecipeIngredientSerializer(serializers.ModelSerializer):
    """A serializer for RecipeIngredient through table model."""

    recipe_name = serializers.ReadOnlyField(source="recipe.name")
    ingredient_name = serializers.ReadOnlyField(source="ingredient.name")

    class Meta:
        model = RecipeIngredient


class RecipeNutrientSerializer(serializers.ModelSerializer):
    recipe_name = serializers.ReadOnlyField(source="recipe.name")
    nutrient_name = serializers.ReadOnlyField(source="nutrient.name")

    class Meta:
        model = RecipeNutrients
