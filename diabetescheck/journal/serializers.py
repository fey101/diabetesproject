from rest_framework import serializers

from .models import (
    Gender,
    MaritalStatus,
    CommunicationLanguage,
    ContactType,
    Medication,
    HealthDetails,
    PersonPhoto,
    Person,
    Contact,
    PersonLanguage,
)


class ContactSerializer(serializers.ModelSerializer):
    person_name = serializers.ReadOnlyField(source='person.__str__')
    contact_type_name = serializers.ReadOnlyField(
        source='contact_type.display')

    class Meta:
        model = Contact


class PersonPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonPhoto


class PersonSerializer(serializers.ModelSerializer):
    person_display = serializers.ReadOnlyField(source='__str__')
    gender_name = serializers.ReadOnlyField(source='gender.display')
    marital_status_name = serializers.ReadOnlyField(
        source='marital_status.display')
    contact_set = ContactSerializer(many=True, read_only=True)
    personphoto_set = PersonPhotoSerializer(many=True, read_only=True)

    class Meta:
        model = Person


class PersonLanguageSerializer(serializers.ModelSerializer):

    class Meta(object):
        model = PersonLanguage


class GenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gender


class MaritalStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaritalStatus


class CommunicationLanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommunicationLanguage


class ContactTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactType


class MedicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medication


class HealthDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthDetails
