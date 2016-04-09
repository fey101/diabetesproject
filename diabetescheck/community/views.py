from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)

from .models import (
    FAQs,
    ExerciseRoutines,
)

from .serializers import (
    FAQsSerializer,
    ExerciseRoutinesSerializer,
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


# class UsersQuestionListView(ListCreateAPIView):

#     queryset = UsersQuestion.objects.all()
#     serializer_class = UsersQuestionSerializer


# class UsersQuestionDetailView(RetrieveUpdateDestroyAPIView):

#     queryset = UsersQuestion.objects.all()
#     serializer_class = UsersQuestionSerializer
#     lookup_field = 'pk'


# class UsersGroupListView(ListCreateAPIView):

#     queryset = UsersGroup.objects.all()
#     serializer_class = UsersGroupSerializer


# class UsersGroupDetailView(RetrieveUpdateDestroyAPIView):

#     queryset = UsersGroup.objects.all()
#     serializer_class = UsersGroupSerializer
#     lookup_field = 'pk'


# class GroupMessageListView(ListCreateAPIView):

#     queryset = GroupMessage.objects.all()
#     serializer_class = GroupMessageSerializer


# class GroupMessageDetailView(RetrieveUpdateDestroyAPIView):

#     queryset = GroupMessage.objects.all()
#     serializer_class = GroupMessageSerializer
#     lookup_field = 'pk'


class ExerciseRoutinesListView(ListCreateAPIView):

    queryset = ExerciseRoutines.objects.all()
    serializer_class = ExerciseRoutinesSerializer


class ExerciseRoutinesDetailView(RetrieveUpdateDestroyAPIView):

    queryset = ExerciseRoutines.objects.all()
    serializer_class = ExerciseRoutinesSerializer
    lookup_field = 'pk'
