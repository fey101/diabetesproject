from rest_framework import serializers

from .models import (
    FAQs,
    ExerciseRoutines,
    SugarLevelDetails,
)


# class UsersQuestionSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UsersQuestion


class FAQsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQs


class ExerciseRoutinesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExerciseRoutines


class SugarLevelDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SugarLevelDetails
