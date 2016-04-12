from rest_framework import serializers

from .models import (
    Gender,
    HealthDetails,
    Person,
    ExerciseLog,
    FoodLog,
    SugarLevelsLog
)


class PersonSerializer(serializers.ModelSerializer):
    person_display = serializers.ReadOnlyField(source='__str__')
    gender_name = serializers.ReadOnlyField(source='gender.display')

    class Meta:
        model = Person


class GenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gender


class HealthDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthDetails


class ExerciseLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExerciseLog


class FoodLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodLog


class SugarLevelsLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = SugarLevelsLog
