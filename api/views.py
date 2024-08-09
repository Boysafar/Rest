from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from api.serializers import ProfileSerializer
from users.models import Profile
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class ProfileDetailSerializer(GenericAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated, ]

    def get(self, request, *args, **kwarg):
        data = {'message': 'Hello World'}
        return Response(data)

