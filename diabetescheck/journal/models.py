import datetime

from django.db import models
from django.utils import timezone
from django.contrib.postgres.fields import ArrayField

from rest_framework.serializers import ValidationError

from diabetescheck_auth.models import User
from community.models import (
    ExerciseRoutines,
    SugarLevelDetails,
)
from recipe.models import Recipe

ACTIVITY_LEVELS = (
    ("low", "Low"),
    ("high", "High"),
    ("moderate", "Moderate"),
    ("in bed", "You spend the whole day in bed/No movements"),
)
EXERCISE_FREQ = (
    ("random", "Random"),
    ("15 min", "15 minutes"),
    ("30 min", "30 minutes"),
    ("1 hr or more", "1 hour/above 1 hour"),
)


class Valueset(models.Model):
    display = models.CharField(max_length=10)

    class Meta(object):
        abstract = True

    def __str__(self):
        return self.display


class Gender(Valueset):
    pass


class HealthDetails(models.Model):
    weight = models.DecimalField(max_digits=10, decimal_places=1)
    height = models.DecimalField(max_digits=10, decimal_places=2)
    diabetic = models.BooleanField()
    related_conditions = ArrayField(
        models.CharField(max_length=10), blank=True, null=True)
    daily_activity_level = models.CharField(
        max_length=255, choices=ACTIVITY_LEVELS)
    exercise_freq = models.CharField(max_length=255, choices=EXERCISE_FREQ)

    errors = []

    @property
    def bmi(self):
        # NB height is in metres
        return round(self.weight / (self.height ** 2), 4)

    @property
    def hbw(self):
        """
        Healthy Body-Weight(HBW).

        Obtained using a bmi of 21 and person's height.
        """
        hbw = 21 * (self.height ** 2)
        return round(hbw)

    # @property
    # def daily_calorie_need(self):
    #     """Amount of calories needed to satisfy activity level lifestyle."""
    #     activity = (self.daily_activity_level, self.exercise_freq)
    #     if activity == ("in bed", "random"):
    #         hbr = 10
    #     elif activity == ("low", "random"):
    #         hbr = 11
    #     elif activity == ("low", "15 min"):
    #         hbr = 12
    #     elif activity == ("low", "30 min"):
    #         hbr = 13
    #     elif activity == ("low", "1 hr or more") or activity == (
    #             "moderate", "random"):
    #             hbr = 14
    #     elif activity == ("moderate", "15 min"):
    #         hbr = 15
    #     elif activity == ("moderate", "30 min"):
    #         hbr = 16
    #     elif activity == ("moderate", "1 hr or more") or activity == (
    #             "high", "random"):
    #             hbr = 17
    #     elif activity == ("high", "15 min"):
    #         hbr = 18
    #     elif activity == ("high", "30 min"):
    #         hbr = 19
    #     elif activity == ("high", "1 hr or more"):
    #         hbr = 20
    #     return 21 * (self.height ** 2) * hbr

    def validate_small_height(self):
        error_msg = "The height value should be positive"
        try:
            self.errors.remove(error_msg)
        except ValueError:
            if self.height < 1:
                self.errors.append(error_msg)

    def validate_max_height(self):
        error_msg = "The height should not be greater than 3 meters"
        try:
            self.errors.remove(error_msg)
        except ValueError:
            if self.height > 3:
                self.errors.append(error_msg)

    def validate_low_weight(self):
        error_msg = "The weight value should be positive"
        try:
            self.errors.remove(error_msg)
        except ValueError:
            if self.weight < 1:
                self.errors.append(error_msg)

    def validate_max_weight(self):
        error_msg = "The weight value should be less than 500 Kilogrammes"
        try:
            self.errors.remove(error_msg)
        except ValueError:
            if self.weight > 500:
                self.errors.append(error_msg)

    def raise_error(self):
        if len(self.errors) > 0:
                errors = self.errors
                self.errors = []
                raise ValidationError(errors)

    def clean(self):
        self.validate_small_height()
        self.validate_max_height()
        self.validate_low_weight()
        self.validate_max_weight()
        self.raise_error()
        super(HealthDetails, self).clean()

    def save(self, *args, **kwargs):
        self.full_clean(exclude=None)
        super(HealthDetails, self).save(*args, **kwargs)


class Person(models.Model):
    """
    A generic person record.

    Demographics and administrative information about a person independent
    of a specific health-related context
    """

    user = models.OneToOneField(User, related_name="person")
    gender = models.ForeignKey(Gender, on_delete=models.PROTECT)
    date_of_birth = models.DateField(verbose_name="Date of birth (YYYY-MM-DD)")
    health_details = models.OneToOneField(
        HealthDetails, null=True, blank=True)
    sugar_logs = models.ManyToManyField(
        SugarLevelDetails, through="DetailedSugarLog")
    exercise_logs = models.ManyToManyField(
        ExerciseRoutines, through="DetailedExerciseLog")
    food_logs = models.ManyToManyField(
        Recipe, through="DetailedFoodLog")

    def get_full_name(self):
        """Return the identifying fullname for this User."""
        return " ".join([self.user.first_name, self.user.last_name])

    def validate_dob(self):
        """
        Check date of birth is within expected limits.

        ... that is date of birth is less than today
        and less than 150 years
        """
        if self.date_of_birth:
            max_age = 365 * 300
            delta = datetime.timedelta(days=max_age)
            if self.date_of_birth > timezone.now().date():
                raise ValidationError(
                    {'date_of_birth': ('Date of birth cannot' +
                                       ' be a future date')})

            oldest_person = timezone.now().date() - delta
            if self.date_of_birth < oldest_person:
                raise ValidationError(
                    {'date_of_birth': ('A person cannot be more than ' +
                                       '300 years old.')})

    def clean(self):
        self.validate_dob()
        super(Person, self).clean()

    def save(self, *args, **kwargs):
        self.full_clean(exclude=None)
        super(Person, self).save(*args, **kwargs)

    def __str__(self):
        return self.get_full_name()


class DetailedExerciseLog(models.Model):
    person = models.ForeignKey(
        Person, related_name="exercise_log_details")
    date = models.DateField(auto_now=True)
    time = models.TimeField(auto_now=True)
    exercise_type = models.ForeignKey(
        ExerciseRoutines, related_name="exercise_details_persons")
    duration = models.DurationField()

    @property
    def total_calories_burnt(self):
        """Calculate calories burnt in activity."""
        weight = self.person.health_details.weight
        minutes = int(self.duration.seconds / 60)
        burnt_calories = self.exercise_type.rate * weight * minutes
        return burnt_calories


class DetailedFoodLog(models.Model):
    person = models.ForeignKey(
        Person, related_name="food_log_details")
    date = models.DateField(auto_now=True)
    time = models.TimeField(auto_now=True)
    food = models.ForeignKey(
        Recipe, related_name="recipe_persons")
    period = models.CharField(max_length=255)
    # the following are in relation to the wholesome period and not just ...
    # a single recipe. i.e one period log might have many recipes and a single
    # recipe can be consumed as more than one serving per period.
    calories_gained = models.DecimalField(max_digits=20, decimal_places=3)
    cholesterol_gained = models.DecimalField(max_digits=20, decimal_places=3)
    recommendation = models.CharField(
        max_length=255, blank=True, null=True)


class DetailedSugarLog(models.Model):
    """A through table for Person - SugarLevelDetails relationship."""
    person = models.ForeignKey(
        Person, related_name="sugar_log_details")
    date = models.DateField(auto_now=True)
    time = models.TimeField(auto_now=True)
    sugarLevel = models.IntegerField()
    period = models.CharField(max_length=255)
    details = models.ForeignKey(
        SugarLevelDetails, related_name="sugarDetails_log")
