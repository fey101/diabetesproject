from django.conf.urls import url

from .views import (
    FAQsListView,
    FAQsDetailView,
    ExerciseRoutinesListView,
    ExerciseRoutinesDetailView,
)


urlpatterns = [
    # url(r'^user_messages/',
    #     UserMessageListView.as_view(), name='user_messages_list'),
    # url(r'^user_message/(?P<pk>[0-9]+)$',
    #     UserMessageDetailView.as_view(), name='user_message_detail'),

    url(r'^FAQs/',
        FAQsListView.as_view(), name='FAQs_list'),
    url(r'^FAQ/(?P<pk>[0-9]+)$',
        FAQsDetailView.as_view(), name='FAQ_detail'),

    # url(r'^user_groups/',
    #     UsersGroupListView.as_view(), name='user_groups_list'),
    # url(r'^user_group/(?P<pk>[0-9]+)$',
    #     UsersGroupDetailView.as_view(), name='user_group_detail'),

    # url(r'^group_messages/',
    #     GroupMessageListView.as_view(), name='group_message_list'),
    # url(r'^group_message/(?P<pk>[0-9]+)$',
    #     GroupMessageDetailView.as_view(), name='group_message_detail'),

    # url(r'^users_questions/',
    #     UsersQuestionListView.as_view(), name='user_questions_list'),
    # url(r'^users_question/(?P<pk>[0-9]+)$',
    #     UsersQuestionDetailView.as_view(), name='users_question_detail'),

    url(r'^exercises/',
        ExerciseRoutinesListView.as_view(), name='exercises_list'),
    url(r'^exercise/(?P<pk>[0-9]+)$',
        ExerciseRoutinesDetailView.as_view(), name='exercise_detail'),
]
