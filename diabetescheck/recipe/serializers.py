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


class NutritionalValueSerializer(serializers.ModelSerializer):
    fooditem_name = serializers.ReadOnlyField(source="food_item.name")
    category_display = serializers.ReadOnlyField(source="category.category")
    calories_in_units_consumed = serializers.ReadOnlyField()

    class Meta:
        model = NutritionalValue


class FoodItemSerializer(serializers.ModelSerializer):
    # calories = serializers.ReadOnlyField()
    fooditem_nutrients = NutritionalValueSerializer(
        many=True, read_only=True)

    class Meta:
        model = FoodItem
        fields = ("id", "name", "description",
                  "nutritional_value", "fooditem_nutrients")


class RecipeSerializer(serializers.ModelSerializer):
    person_name = serializers.StringRelatedField(source="person")
    ingredients_list = FoodItemSerializer(many=True, read_only=True)

    class Meta:
        model = Recipe
        fields = ("id", "name", "description", "instructions", "prep_time",
                  "serving", "person", "person_name", "ingredients",
                  "ingredients_list")


class FoodCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodCategory
