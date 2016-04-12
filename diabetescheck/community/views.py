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


class FAQsDetailView(RetrieveUpdateDestroyAPIView):

    queryset = FAQs.objects.all()
    serializer_class = FAQsSerializer
    lookup_field = 'pk'


class ExerciseRoutinesListView(ListCreateAPIView):

    queryset = ExerciseRoutines.objects.all()
    serializer_class = ExerciseRoutinesSerializer


class ExerciseRoutinesDetailView(RetrieveUpdateDestroyAPIView):

    queryset = ExerciseRoutines.objects.all()
    serializer_class = ExerciseRoutinesSerializer
    lookup_field = 'pk'


class SugarLevelsDetailsListView(ListCreateAPIView):

    queryset = SugarLevelDetails.objects.all()
    serializer_class = SugarLevelDetailsSerializer


class SugarLevelsDetailsDetailView(RetrieveUpdateDestroyAPIView):

    queryset = SugarLevelDetails.objects.all()
    serializer_class = SugarLevelDetailsSerializer
    lookup_field = 'pk'
