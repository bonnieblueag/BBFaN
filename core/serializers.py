from rest_framework import serializers
from django.contrib.auth.models import User
from core import models as CoreModels




class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'is_staff', 'is_active', 'date_joined')

class SpeciesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CoreModels.Species
        fields = ('id', 'name')

class CultivarSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CoreModels.Cultivar
        fields = ('id', 'species', 'name', 'ripens', 'origin', 'origin_date', 'uses', 'is_pollen_sterile')

class LocationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CoreModels.Location
        fields = ('id', 'center', 'state', 'country', 'latitude', 'longitude')

class FruitUseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CoreModels.FruitUse
        fields = ('id', 'use')

class RootstockSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CoreModels.Rootstock
        fields = ('id', 'species', 'name', 'max_height', 'max_width', 'dwarfing')
