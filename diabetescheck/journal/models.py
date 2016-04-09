import datetime

from django.db import models
from django.utils import timezone

from rest_framework.serializers import ValidationError

from diabetescheck_auth.models import User
from community.models import ExerciseRoutines
from recipe.models import Recipe


class Valueset(models.Model):
    display = models.CharField(max_length=10)

    class Meta(object):
        abstract = True

    def __str__(self):
        return self.display


class Gender(Valueset):
    pass


class Person(models.Model):
    """
    A generic person record.

    Demographics and administrative information about a person independent
    of a specific health-related context
    """

    user = models.OneToOneField(User)
    gender = models.ForeignKey(Gender, on_delete=models.PROTECT)
    date_of_birth = models.DateField(verbose_name="Date of birth (YYYY-MM-DD)")
    health_details = models.OneToOneField(
        'HealthDetails', null=True, blank=True)

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


class HealthDetails(models.Model):
    weight = models.DecimalField(max_digits=10, decimal_places=4)
    height = models.DecimalField(max_digits=10, decimal_places=4)
    diabetic = models.BooleanField()

    errors = []

    @property
    def bmi(self):
        return self.weight / ((self.height / 100) ** 2)

    def validate_small_height(self):
        error_msg = "The height value should be positive"
        try:
            self.errors.remove(error_msg)
        except ValueError:
            if self.height < 1:
                self.errors.append(error_msg)

    def validate_max_height(self):
        error_msg = "The height should not be greater than 300 centimeters"
        try:
            self.errors.remove(error_msg)
        except ValueError:
            if self.height > 300:
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
        self.validate_low_pulse()
        self.validate_high_pulse()
        self.validate_diastolic_bp()
        self.validate_systolic_bp()
        self.validate_systolic_diastolic()
        self.validate_small_height()
        self.validate_max_height()
        self.validate_low_weight()
        self.validate_max_weight()
        self.raise_error()
        super(HealthDetails, self).clean()

    def save(self, *args, **kwargs):
        self.full_clean(exclude=None)
        super(HealthDetails, self).save(*args, **kwargs)


class ExerciseLog(models.Model):
    person = models.ForeignKey(Person)
    date = models.DateField(auto_now=True)
    duration = models.DurationField()
    exercise_type = models.ForeignKey(ExerciseRoutines)
    calories_lost = models.CharField(
        max_length=255, blank=True, null=True)


class FoodLog(models.Model):
    person = models.ForeignKey(Person)
    date = models.DateField(auto_now=True)
    time = models.CharField(max_length=255)
    food = models.ForeignKey(Recipe)
    calories_gained = models.DecimalField(max_digits=20, decimal_places=3)
    recommendation = models.CharField(
        max_length=255, blank=True, null=True)


class SugarLevelsLog(models.Model):
    person = models.ForeignKey(Person)
    date = models.DateField(auto_now=True)
    time = models.CharField(max_length=255)
    sugar_level = models.DecimalField(max_digits=20, decimal_places=3)
    recommendation = models.CharField(
        max_length=255, blank=True, null=True)
