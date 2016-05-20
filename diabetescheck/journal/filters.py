import django_filters

from .models import (
    DetailedFoodLog
)


class DetailedFoodLogFilter(django_filters.FilterSet):
    date = django_filters.DateTimeFilter(name="date",lookup_type="gte")

    class Meta:
        model = DetailedFoodLog
