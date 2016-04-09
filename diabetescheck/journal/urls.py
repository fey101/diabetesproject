from django.conf.urls import url

from .views import (
    GenderListView,
    GenderDetailView,
    HealthDetailsListView,
    HealthDetailsDetailView,
    PersonListView,
    PersonListDetailView,
    FoodLogListView,
    FoodLogDetailView,
    ExerciseLogListView,
    ExerciseLogDetailView,
    SugarLevelsLogListView,
    SugarLevelsLogDetailView,
)

urlpatterns = [
    url(r'^persons/$', PersonListView.as_view(),
        name='persons'),
    url(r'^persons/(?P<pk>[^/]+)/$', PersonListDetailView.as_view(),
        name='persons_detail'),

    url(r'^gender/$', GenderListView.as_view(), name='gender'),
    url(r'^gender/(?P<pk>[^/]+)/$', GenderDetailView.as_view(),
        name='gender_detail'),

    url(r'^health_details/$', HealthDetailsListView.as_view(),
        name='health_details'),
    url(r'^health_details/(?P<pk>[^/]+)/$', HealthDetailsDetailView.as_view(),
        name='health_details_detail'),

    url(r'^foodlogs/$', FoodLogListView.as_view(),
        name='foodlogs'),
    url(r'^foodlog/(?P<pk>[^/]+)/$', FoodLogDetailView.as_view(),
        name='foodlog_detail'),

    url(r'^exerciselogs/$', ExerciseLogListView.as_view(),
        name='exerciselogs'),
    url(r'^exerciselog/(?P<pk>[^/]+)/$', ExerciseLogDetailView.as_view(),
        name='exerciselog_detail'),

    url(r'^sugarlevelslogs/$', SugarLevelsLogListView.as_view(),
        name='sugarlevelslogs'),
    url(r'^sugarlevelslog/(?P<pk>[^/]+)/$', SugarLevelsLogDetailView.as_view(),
        name='sugarlevel_detail'),

]
