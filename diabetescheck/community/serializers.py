from rest_framework import serializers

from .models import (
    FAQs,
    ExerciseRoutines,
)


# class UsersQuestionSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UsersQuestion


class FAQsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQs


# class UsersGroupSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UsersGroup


# class UserMessageSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UserMessage


# class GroupMessageSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = GroupMessage


class ExerciseRoutinesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExerciseRoutines
