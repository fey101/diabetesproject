from django.conf.urls import url

from .views import (
    UserListView,
    UserDetailView,
    OauthApplicationListView,
    OauthApplicationDetailView,
)


urlpatterns = [
    url(r'^users/', UserListView.as_view(), name='users_list'),
    url(r'^users/(?P<pk>[0-9]+)$',
        UserDetailView.as_view(), name='users_detail'),

    url(r'^applications/',
        OauthApplicationListView.as_view(), name='applications_list'),
    url(r'^applications/(?P<pk>[0-9]+)$',
        OauthApplicationDetailView.as_view(), name='applications_detail'),
]
