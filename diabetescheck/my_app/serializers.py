# from django.contrib.auth.models import User, Group
# from rest_framework import serializers
# from my_app import models


# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ('url', 'username', 'email', 'groups')


# class GroupSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Group
#         fields = ('url', 'name')


# class AbstractBaseSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.AbstractBase
#         abstract = True


# class FrequentlyAskedQuestionsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.FrequentlyAskedQuestions
#         lookup_field = 'pk'


# class UserBasicDetailsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.UserBasicDetails
#         lookup_field = 'pk'


# class UserHealthDetailsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.UserHealthDetails
#         lookup_field = 'pk'


# class MedicationSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.Medication
#         lookup_field = 'pk'


# class CalendarSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.Calendar
#         lookup_field = 'pk'


# class FoodItemSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.FoodItem
#         lookup_field = 'Pk'


# class RecipeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.Recipe
#         lookup_field = 'pk'
