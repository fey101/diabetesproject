from rest_framework import serializers


from .models import (
    User,
    OauthApplication,
)
from journal.serializers import (
    HealthDetailsSerializer,
    PersonSerializer,
)


class UserSerializer(serializers.ModelSerializer):
    person = PersonSerializer()
    person_health = HealthDetailsSerializer(source="person.health_details")

    class Meta:
        model = User


class OauthApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = OauthApplication
