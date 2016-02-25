from django.conf.urls import url

from .views import (
    GenderListView,
    GenderDetailView,
    MaritalStatusListView,
    MaritalStatusDetailView,
    CommunicationLanguageListView,
    CommunicationLanguageDetailView,
    ContactTypeListView,
    ContactTypeDetailView,
    MedicationListView,
    MedicationDetailView,
    HealthDetailsListView,
    HealthDetailsDetailView,
    # PersonPhotoListView,
    # PersonPhotoDetailView,
    PersonListView,
    PersonListDetailView,
    ContactListView,
    ContactDetailView,
    PersonLanguageListView,
    PersonLanguageDetailView,
)

urlpatterns = [
    url(r'^persons/$', PersonListView.as_view(),
        name='persons'),
    url(r'^persons/(?P<pk>[^/]+)/$', PersonListDetailView.as_view(),
        name='persons_detail'),

    url(r'^contacts/$', ContactListView.as_view(),
        name='contacts'),
    url(r'^contacts/(?P<pk>[^/]+)/$', ContactDetailView.as_view(),
        name='contacts_detail'),

    # url(r'^user_photo/$', PersonPhotoListView.as_view(),
    #     name='user_photo'),
    # url(r'^user_photo/(?P<pk>[^/]+)/$', PersonPhotoDetailView.as_view(),
    #     name='user_photo_detail'),

    url(r'^person_languages/$', PersonLanguageListView.as_view(),
        name='person_language_list'),
    url(r'^person_languages/(?P<pk>[^/]+)/$',
        PersonLanguageDetailView.as_view(), name='person_language_detail'),

    url(r'^gender/$', GenderListView.as_view(), name='gender'),
    url(r'^gender/(?P<pk>[^/]+)/$', GenderDetailView.as_view(),
        name='gender_detail'),

    url(r'^marital_status/$', MaritalStatusListView.as_view(),
        name='marital_status'),
    url(r'^marital_status/(?P<pk>[^/]+)/$', MaritalStatusDetailView.as_view(),
        name='marital_status_detail'),

    url(r'^languages/$', CommunicationLanguageListView.as_view(),
        name='languages'),
    url(r'^languages/(?P<pk>[^/]+)/$',
        CommunicationLanguageDetailView.as_view(),
        name='languages_detail'),

    url(r'^contact_types/$', ContactTypeListView.as_view(),
        name='contact_types'),
    url(r'^contact_types/(?P<pk>[^/]+)/$', ContactTypeDetailView.as_view(),
        name='contact_types_detail'),

    url(r'^medications/$', MedicationListView.as_view(), name='medications'),
    url(r'^medications/(?P<pk>[^/]+)/$', MedicationDetailView.as_view(),
        name='medications_detail'),

    url(r'^health_details/$', HealthDetailsListView.as_view(),
        name='health_details'),
    url(r'^health_details/(?P<pk>[^/]+)/$', HealthDetailsDetailView.as_view(),
        name='health_details_detail'),
]
