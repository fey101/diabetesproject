from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView

from .serializers import (
    GenderSerializer,
    HealthDetailsSerializer,
    PersonSerializer,
    ExerciseLogSerializer,
    FoodLogSerializer,
    SugarLevelsLogSerializer,
)

from .models import (
    Gender,
    HealthDetails,
    Person,
    DetailedExerciseLog,
    DetailedFoodLog,
    DetailedSugarLog,
)


class PersonListView(ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    ordering_fields = ('first_name', 'last_name', 'date_of_birth')
    search_field = '@search_index'


class PersonListDetailView(RetrieveUpdateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class GenderListView(ListCreateAPIView):
    queryset = Gender.objects.all()
    serializer_class = GenderSerializer


class GenderDetailView(RetrieveUpdateAPIView):
    queryset = Gender.objects.all()
    serializer_class = GenderSerializer


class HealthDetailsListView(ListCreateAPIView):
    queryset = HealthDetails.objects.all()
    serializer_class = HealthDetailsSerializer


class HealthDetailsDetailView(RetrieveUpdateAPIView):
    queryset = HealthDetails.objects.all()
    serializer_class = HealthDetailsSerializer


class FoodLogListView(ListCreateAPIView):
    queryset = DetailedFoodLog.objects.all()
    serializer_class = FoodLogSerializer


class FoodLogDetailView(RetrieveUpdateAPIView):
    queryset = DetailedFoodLog.objects.all()
    serializer_class = FoodLogSerializer


class ExerciseLogListView(ListCreateAPIView):
    queryset = DetailedExerciseLog.objects.all()
    serializer_class = ExerciseLogSerializer


class ExerciseLogDetailView(RetrieveUpdateAPIView):
    queryset = DetailedExerciseLog.objects.all()
    serializer_class = ExerciseLogSerializer


class SugarLevelsLogListView(ListCreateAPIView):
    queryset = DetailedSugarLog.objects.all()
    serializer_class = SugarLevelsLogSerializer


class SugarLevelsLogDetailView(RetrieveUpdateAPIView):
    queryset = DetailedSugarLog.objects.all()
    serializer_class = SugarLevelsLogSerializer
