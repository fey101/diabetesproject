from rest_framework import serializers


from .models import (
    Recipe,
    FoodItem,
    FoodCategory,
    FoodItemCategory
)


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe


class FoodItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodItem


class FoodCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodCategory


class FoodItemCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodItemCategory
