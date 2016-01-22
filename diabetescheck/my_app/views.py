# from django.contrib.auth.models import User, Group

# from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
# from rest_framework import viewsets
# from tutorial.quickstart.serializers import UserSerializer, GroupSerializer
# from my_app import models


# class UserViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = User.objects.all().order_by('-date_joined')
#     serializer_class = UserSerializer


# class GroupViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows groups to be viewed or edited.
#     """
#     queryset = Group.objects.all()
#     serializer_class = GroupSerializer

# class UserBasicDetailsView(RetrieveUpdateAPIView):
#     permissions = {
#         'PUT': ['common.organisation.list_organisation'],
#         'PATCH': ['common.organisation.create_organisation']
#     }
#     queryset = models.UserBasicDetails.objects.all()
#     serializer_class = OrganisationSerializer
#     filter_class = OrganisationFilter
#     ordering_fields = ('organisation_name', 'code')
