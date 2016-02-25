from rest_framework import serializers


from .models import (
    Recipe,
    FoodItem,
    FoodCategory,
    NutritionalValue
)


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
