from django.contrib.auth.models import User
from images.serializers import *
from images.models import *

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action


class ResponsiveImageViewSet(viewsets.ModelViewSet):
    queryset = ResponsiveImage.objects.all()
    serializer_class = ResponsiveImageSerializer
    lookup_field = 'slug'