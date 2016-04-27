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
        read_only_fields = ('last_login', )
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class OauthApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = OauthApplication
