from rest_framework import serializers


from .models import (
    Recipe,
    FoodItem,
    RecipeFoodItem,
    FoodCategory,
    NutritionalValue
)


class RecipeFoodItemSerializer(serializers.ModelSerializer):
    """A serializer for RecipeFoodItem through table model."""

    recipe_name = serializers.ReadOnlyField(source="recipe.name")
    fooditem_name = serializers.ReadOnlyField(source="food_item.name")

    class Meta:
        model = RecipeFoodItem


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe


class NutritionalValueSerializer(serializers.ModelSerializer):
    fooditem_name = serializers.ReadOnlyField(source="food_item.name")
    category_display = serializers.ReadOnlyField(source="category.category")

    class Meta:
        model = NutritionalValue


class FoodItemSerializer(serializers.ModelSerializer):
    calories = serializers.ReadOnlyField()
    fooditem_nutrients = NutritionalValueSerializer(
        many=True, read_only=True)

    class Meta:
        model = FoodItem


class FoodCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodCategory
