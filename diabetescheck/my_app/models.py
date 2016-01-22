# from django.db import models


# CONSTANTS = {
#     'CALORIC_VALUE_PER_GRAM': {
#         # vitamins: 4,
#         'protein': 4,
#         'carbohydrates': 4,
#         'fat': 9
#     }
# }


# class AbstractBase(models.Model):
#     active = models.BooleanField(default=True)
#     deleted = models.BooleanField(default=False)
#     created = models.DateTimeField()
#     updated = models.DateTimeField()


# class FrequentlyAskedQuestions(AbstractBase):
#     Question = models.CharField(max_length=255)
#     Response = models.TextField()


# class UserBasicDetails(AbstractBase):
#     GENDER_CHOICES = (
#         ('M', 'Male'),
#         ('F', 'Female'),
#     )
#     name = models.CharField(max_length=255)
#     gender = models.CharField(
#         max_length=1, choices=GENDER_CHOICES, default='M')
#     date_of_birth = models.DateField()
#     email = models.EmailField()
#     phone_number = models.CharField(max_length=255)
#     diabetic = models.BooleanField(default=False)


# class UserHealthDetails(AbstractBase):
#     weight = models.DecimalField(decimal_places=4)
#     abdominal_girth = models.DecimalField(decimal_places=2)
#     blood_glucose = models.DecimalField(decimal_places=4)


# class Medication(AbstractBase):
#     pass


# class Calendar(AbstractBase):
#     AVAILABLE_PERIODS = (
#         (),
#         (),
#     )
#     day = models.DateField()
#     period = models.CharField(max_length=255, choices=AVAILABLE_PERIODS)


# class FoodItem(AbstractBase):
#     item_name = models.CharField(max_length=255)
#     fat_content = models.DecimalField(decimal_places=4)
#     protein = models.DecimalField(decimal_places=4)


# class Recipe(AbstractBase):
#     name = models.CharField(max_length=255)
#     ingredients = models.ManyToManyField(FoodItem)
#     instructions = models.TextField()
