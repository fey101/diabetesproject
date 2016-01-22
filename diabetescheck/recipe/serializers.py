from rest_framework import serializers


from .models import (
    Recipe,
    FoodItem
)


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe


class FoodItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodItem
