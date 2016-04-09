from django.db import models


class FAQs(models.Model):
    """Questions not associated with any particular users..

    This is because these questions tend to cut across almost all users
    """

    question = models.CharField(max_length=255)
    brief_response = models.TextField()
    detailed_response = models.TextField(null=True, blank=True)


class ExerciseRoutines(models.Model):
    """Known documented facts about different exercises."""

    name = models.CharField(max_length=255)
    duration = models.DurationField()
    calories_burnt = models.DecimalField(decimal_places=2, max_digits=5)
