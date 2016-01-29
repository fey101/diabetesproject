from django.conf.urls import url

from .views import (
    UserMessageListView,
    UserMessageDetailView,
    UsersGroupListView,
    UsersGroupDetailView,
    GroupMessageListView,
    GroupMessageDetailView,
    UsersQuestionListView,
    UsersQuestionDetailView,
)


urlpatterns = [
    url(r'^user_messages/',
        UserMessageListView.as_view(), name='user_messages_list'),
    url(r'^user_message/(?P<pk>[0-9]+)$',
        UserMessageDetailView.as_view(), name='user_message_detail'),

    url(r'^user_groups/',
        UsersGroupListView.as_view(), name='user_groups_list'),
    url(r'^user_group/(?P<pk>[0-9]+)$',
        UsersGroupDetailView.as_view(), name='user_group_detail'),

    url(r'^group_messages/',
        GroupMessageListView.as_view(), name='group_message_list'),
    url(r'^group_message/(?P<pk>[0-9]+)$',
        GroupMessageDetailView.as_view(), name='group_message_detail'),

    url(r'^users_questions/',
        UsersQuestionListView.as_view(), name='user_questions_list'),
    url(r'^users_question/(?P<pk>[0-9]+)$',
        UsersQuestionDetailView.as_view(), name='users_question_detail'),
]
