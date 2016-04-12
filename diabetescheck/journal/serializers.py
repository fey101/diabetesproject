from rest_framework import serializers

from .models import (
    Gender,
    HealthDetails,
    Person,
    DetailedExerciseLog,
    DetailedFoodLog,
    DetailedSugarLog
)


class HealthDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthDetails


class PersonSerializer(serializers.ModelSerializer):
    person_display = serializers.ReadOnlyField(source='__str__')
    gender_name = serializers.ReadOnlyField(source='gender.display')
    person_health = HealthDetailsSerializer(
        source="health_details", read_only=True)

    class Meta:
        model = Person


class GenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gender


class ExerciseLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetailedExerciseLog


class FoodLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetailedFoodLog


class SugarLevelsLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetailedSugarLog
