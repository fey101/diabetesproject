from rest_framework import serializers


from .models import (
    User,
    OauthApplication,
)
from journal.serializers import (
    PersonSerializer,
)


class UserSerializer(serializers.ModelSerializer):
    person = PersonSerializer(read_only=True)

    class Meta:
        model = User


class OauthApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = OauthApplication
