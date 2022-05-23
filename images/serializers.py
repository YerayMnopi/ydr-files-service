from rest_framework import serializers
from images.models import *
from django.contrib.auth.models import User


class ResponsiveImageSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = ResponsiveImage
        fields = '__all__'
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }
