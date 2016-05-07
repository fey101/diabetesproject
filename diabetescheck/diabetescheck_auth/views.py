from django.contrib.auth import get_user_model
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    RetrieveAPIView,
)

from .models import (
    User,
    OauthApplication,
)

from .serializers import (
    UserSerializer,
    OauthApplicationSerializer,
)

from .permissions import IsAuthenticatedOrCreate


class UserListView(ListCreateAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticatedOrCreate,)


class UserDetailView(RetrieveUpdateDestroyAPIView):

    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    lookup_field = 'id'


class OauthApplicationListView(ListCreateAPIView):

    queryset = OauthApplication.objects.all()
    serializer_class = OauthApplicationSerializer


class OauthApplicationDetailView(RetrieveUpdateDestroyAPIView):

    queryset = OauthApplication.objects.all()
    serializer_class = OauthApplicationSerializer
    lookup_field = 'pk'


class MeView(RetrieveAPIView):
    """A view showing only the details of logged in user."""

    queryset = None
    serializer_class = UserSerializer

    def get_object(self):
        """The queryset equivalent."""
        return self.request.user
