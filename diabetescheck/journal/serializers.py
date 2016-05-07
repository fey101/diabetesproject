from rest_framework import serializers

from .models import (
    Gender,
    HealthDetails,
    Person,
    DetailedExerciseLog,
    DetailedFoodLog,
    DetailedSugarLog
)


class PersonFieldMixin(serializers.ModelSerializer):
    """.

    Automates provision of fields such as person
    which always depends on logged in user.
    """

    person = serializers.CharField(read_only=True)

    def create(self, validated_data):
        """.

        Injects the fields in the abstract base model as a model
        instance is being saved.
        """
        user = self.context['request'].user
        validated_data['person'] = user.person

        return self.Meta.model.objects.create(**validated_data)


class HealthDetailsSerializer(serializers.ModelSerializer):
    bmi = serializers.ReadOnlyField()
    hbw = serializers.ReadOnlyField()
    daily_calorie_need = serializers.ReadOnlyField()

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


class ExerciseLogSerializer(PersonFieldMixin):
    exercise_type_name = serializers.ReadOnlyField(
        source="exercise_type.__str__")
    total_calories_burnt = serializers.ReadOnlyField()

    class Meta:
        model = DetailedExerciseLog


class FoodLogSerializer(PersonFieldMixin):
    class Meta:
        model = DetailedFoodLog


class SugarLevelsLogSerializer(PersonFieldMixin):
    class Meta:
        model = DetailedSugarLog
