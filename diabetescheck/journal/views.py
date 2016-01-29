from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework.parsers import MultiPartParser

from .serializers import (
    GenderSerializer,
    MaritalStatusSerializer,
    CommunicationLanguageSerializer,
    ContactTypeSerializer,
    MedicationSerializer,
    HealthDetailsSerializer,
    PersonIDSerializer,
    PersonPhotoSerializer,
    PersonSerializer,
    ContactSerializer,
    PersonLanguageSerializer,
)

from .models import (
    Gender,
    MaritalStatus,
    CommunicationLanguage,
    ContactType,
    Medication,
    HealthDetails,
    PersonID,
    PersonPhoto,
    Person,
    Contact,
    PersonLanguage,
)


class PersonListView(ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    ordering_fields = ('first_name', 'last_name', 'date_of_birth')
    search_field = '@search_index'


class PersonListDetailView(RetrieveUpdateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class ContactListView(ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class ContactDetailView(RetrieveUpdateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class PersonIDListView(ListCreateAPIView):
    queryset = PersonID.objects.all()
    serializer_class = PersonIDSerializer


class PersonIDDetailView(RetrieveUpdateAPIView):
    queryset = PersonID.objects.all()
    serializer_class = PersonIDSerializer


class PersonPhotoListView(ListCreateAPIView):
    queryset = PersonPhoto.objects.all()
    serializer_class = PersonPhotoSerializer
    parser_classes = (MultiPartParser, )


class PersonPhotoDetailView(RetrieveUpdateAPIView):
    queryset = PersonPhoto.objects.all()
    serializer_class = PersonPhotoSerializer


class PersonLanguageListView(ListCreateAPIView):
    queryset = PersonLanguage.objects.all()
    serializer_class = PersonLanguageSerializer


class PersonLanguageDetailView(RetrieveUpdateAPIView):
    queryset = PersonLanguage.objects.all()
    serializer_class = PersonLanguageSerializer


class GenderListView(ListCreateAPIView):
    queryset = Gender.objects.all()
    serializer_class = GenderSerializer


class GenderDetailView(RetrieveUpdateAPIView):
    queryset = Gender.objects.all()
    serializer_class = GenderSerializer


class MaritalStatusListView(ListCreateAPIView):
    queryset = MaritalStatus.objects.all()
    serializer_class = MaritalStatusSerializer


class MaritalStatusDetailView(RetrieveUpdateAPIView):
    queryset = MaritalStatus.objects.all()
    serializer_class = MaritalStatusSerializer


class CommunicationLanguageListView(ListCreateAPIView):
    queryset = CommunicationLanguage.objects.all()
    serializer_class = CommunicationLanguageSerializer


class CommunicationLanguageDetailView(RetrieveUpdateAPIView):
    queryset = CommunicationLanguage.objects.all()
    serializer_class = CommunicationLanguageSerializer


class ContactTypeListView(ListCreateAPIView):
    queryset = ContactType.objects.all()
    serializer_class = ContactTypeSerializer


class ContactTypeDetailView(RetrieveUpdateAPIView):
    queryset = ContactType.objects.all()
    serializer_class = ContactTypeSerializer


class MedicationListView(ListCreateAPIView):
    queryset = Medication.objects.all()
    serializer_class = MedicationSerializer


class MedicationDetailView(RetrieveUpdateAPIView):
    queryset = Medication.objects.all()
    serializer_class = MedicationSerializer


class HealthDetailsListView(ListCreateAPIView):
    queryset = HealthDetails.objects.all()
    serializer_class = HealthDetailsSerializer


class HealthDetailsDetailView(RetrieveUpdateAPIView):
    queryset = HealthDetails.objects.all()
    serializer_class = HealthDetailsSerializer
