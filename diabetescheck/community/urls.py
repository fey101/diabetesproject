from django.conf.urls import url

from .views import (
    FAQsListView,
    FAQsDetailView,
    ExerciseRoutinesListView,
    ExerciseRoutinesDetailView,
    SugarLevelsDetailsListView,
    SugarLevelsDetailsDetailView,
)


urlpatterns = [

    url(r'^FAQs/',
        FAQsListView.as_view(), name='FAQs_list'),
    url(r'^FAQ/(?P<pk>[0-9]+)$',
        FAQsDetailView.as_view(), name='FAQ_detail'),

    # url(r'^users_questions/',
    #     UsersQuestionListView.as_view(), name='user_questions_list'),
    # url(r'^users_question/(?P<pk>[0-9]+)$',
    #     UsersQuestionDetailView.as_view(), name='users_question_detail'),

    url(r'^exercises/',
        ExerciseRoutinesListView.as_view(), name='exercises_list'),
    url(r'^exercise/(?P<pk>[0-9]+)$',
        ExerciseRoutinesDetailView.as_view(), name='exercise_detail'),

    url(r'^sugarlevel_details/',
        SugarLevelsDetailsListView.as_view(), name='sugarlevels_details_list'),
    url(r'^sugarlevel_detail/(?P<pk>[0-9]+)$',
        SugarLevelsDetailsDetailView.as_view(), name='sugarlevel_detail'),
]
