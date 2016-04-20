from django.db import models

PERIOD_SET = (
    ("before meal", "Before meal"),
    ("after meal", "After meal"),
    ("fasting glucose", "Fasting glucose"),
    ("any", "Any")
)
STATUS_SET = (
    ("Hypoglycemia", "Hypo"),
    ("Normal blood sugar level", "Normal"),
    ("Hyperglycemia", "Hyper")
)


class FAQs(models.Model):
    """Questions not associated with any particular users..

    This is because these questions tend to cut across almost all users
    """

    question = models.CharField(max_length=255, unique=True)
    brief_response = models.TextField()
    detailed_response_url = models.URLField(
        max_length=400, null=True, blank=True)


class ExerciseRoutines(models.Model):
    """Known documented facts about different exercises."""

    name = models.CharField(max_length=255)
    # rate = Calories burned per pound per minute
    rate = models.DecimalField(decimal_places=3, max_digits=5)

    def __str__(self):
        """Class string representation."""
        return self.name


class SugarLevelDetails(models.Model):
    """Holds fixed relations on sugar levels and related implications."""

    period = models.CharField(max_length=15, choices=PERIOD_SET)
    sugarLevel = models.CharField(max_length=10)
    # the diabetic status of patient will determine recommendation given.
    diabetic = models.BooleanField(default=False)
    status = models.CharField(max_length=255, choices=STATUS_SET)
    explanation = models.CharField(max_length=255)
    remedial_action = models.CharField(max_length=255)
    recommendation = models.CharField(max_length=255)
