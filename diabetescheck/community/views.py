from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)

from .models import (
    FAQs,
    ExerciseRoutines,
    SugarLevelDetails,
)

from .serializers import (
    FAQsSerializer,
    ExerciseRoutinesSerializer,
    SugarLevelDetailsSerializer,
)

from .filters import (
    FAQsFilter,
    ExerciseRoutinesFilter,
    SugarLevelDetailsFilter,
)


# class UserMessageListView(ListCreateAPIView):

#     queryset = UserMessage.objects.all()
#     serializer_class = UserMessageSerializer


# class UserMessageDetailView(RetrieveUpdateDestroyAPIView):

#     queryset = UserMessage.objects.all()
#     serializer_class = UserMessageSerializer
#     lookup_field = 'pk'


class FAQsListView(ListCreateAPIView):

    queryset = FAQs.objects.all()
    serializer_class = FAQsSerializer
    filter_class = FAQsFilter


class FAQsDetailView(RetrieveUpdateDestroyAPIView):

    queryset = FAQs.objects.all()
    serializer_class = FAQsSerializer
    lookup_field = 'pk'


class ExerciseRoutinesListView(ListCreateAPIView):

    queryset = ExerciseRoutines.objects.all()
    serializer_class = ExerciseRoutinesSerializer
    filter_class = ExerciseRoutinesFilter


class ExerciseRoutinesDetailView(RetrieveUpdateDestroyAPIView):

    queryset = ExerciseRoutines.objects.all()
    serializer_class = ExerciseRoutinesSerializer
    lookup_field = 'pk'


class SugarLevelsDetailsListView(ListCreateAPIView):

    queryset = SugarLevelDetails.objects.all()
    serializer_class = SugarLevelDetailsSerializer
    filter_class = SugarLevelDetailsFilter


class SugarLevelsDetailsDetailView(RetrieveUpdateDestroyAPIView):

    queryset = SugarLevelDetails.objects.all()
    serializer_class = SugarLevelDetailsSerializer
    lookup_field = 'pk'
