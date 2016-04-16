import django_filters

from .models import (
    FAQs,
    ExerciseRoutines,
    SugarLevelDetails,
)


class FAQsFilter(django_filters.FilterSet):
    class Meta:
        model = FAQs


class ExerciseRoutinesFilter(django_filters.FilterSet):
    class Meta:
        model = ExerciseRoutines


class SugarLevelDetailsFilter(django_filters.FilterSet):
    class Meta:
        model = SugarLevelDetails
