from rest_framework import serializers


from .models import (
    UsersQuestion,
    UsersGroup,
    UserMessage,
    GroupMessage,
)


class UsersQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsersQuestion


class UsersGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsersGroup


class UserMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserMessage


class GroupMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupMessage
