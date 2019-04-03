from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.renderers import BrowsableAPIRenderer
from rest_framework import permissions
from rest_framework.generics import CreateAPIView

from django.contrib.auth import get_user_model
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope

from users.models import Profile
from users.serializers import ProfileSerializer
from users.serializers import UserSerializer


class CreateUserView(CreateAPIView):

    model = get_user_model()
    permission_classes = [
        permissions.AllowAny  # this needs to be here so anonymous users can create a new user
    ]
    serializer_class = UserSerializer

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            print(request.data)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SingleUserProfileDetail(APIView):
    """
    Dictates the data the user is able to see and save
    to their profile.
    """
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope, ]

    def get_user_profile(self):
        """
        Given that the request is coming from a given user,
        go out to the database and request that users profile.
        :return: A profile object
        """
        try:
            return Profile.objects.get(owner=self.request.user)
        except Profile.DoesNotExist:
            raise Http404

    def get(self, request, format=None):
        """
        Get the user's profile and return in a response.
        :param request:
        :param format:
        :return: A response of the user's profile.
        """
        profile = self.get_user_profile()
        return Response(ProfileSerializer(profile).data)

    def post(self, request, format=None):
        """
        Update the user's profile with the info they
        provided in their request.
        :param request:
        :param format:
        :return: A response of the a pass or fail.
        """
        current_profile = self.get_user_profile()
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.update(current_profile, serializer.validated_data)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# DEVELOPER TOOLS FOR LOOKING AT DATABASE#######
##################################################
class ProfileSet(viewsets.ModelViewSet):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
    permission_classes = [
        permissions.AllowAny  # Or anon users can't register
    ]


def index(request):
    return HttpResponse("users index...")
