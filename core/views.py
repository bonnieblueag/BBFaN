from django.shortcuts import render
from rest_framework import routers, viewsets, filters, status
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponseNotFound, JsonResponse, HttpResponse
from django.views.generic import TemplateView, View
from django.forms.models import model_to_dict
from core import models as CoreModels
from core import serializers as CoreSerializers



class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        #context['sites'] = CoreModels.Entity.get_entity_sites()
        return context


def get_species_with_cultivars(request, speciesID):
    site = CoreModels.Species.objects.get(id=speciesID)
    cultivars = CoreModels.Cultivar.objects.filter(species_id=speciesID)
    data = {}
    for model in cultivars:
        data['cultivars'].append(model_to_dict(model))
    return JsonResponse(data)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = CoreSerializers.UserSerializer
    filter_fields = CoreModels.get_fields(User)
    filter_backends = (filters.DjangoFilterBackend, filters.OrderingFilter)

class SpeciesViewSet(viewsets.ModelViewSet):
    queryset = CoreModels.Species.objects.all()
    serializer_class = CoreSerializers.SpeciesSerializer
    filter_fields = CoreModels.get_fields(CoreModels.Species)
    filter_backends = (filters.DjangoFilterBackend, filters.OrderingFilter)

class CultivarViewSet(viewsets.ModelViewSet):
    queryset = CoreModels.Cultivar.objects.all()
    serializer_class = CoreSerializers.CultivarSerializer
    filter_fields = CoreModels.get_fields(CoreModels.Cultivar)
    filter_backends = (filters.DjangoFilterBackend, filters.OrderingFilter)

class FruitUseViewSet(viewsets.ModelViewSet):
    queryset = CoreModels.FruitUse.objects.all()
    serializer_class = CoreSerializers.FruitUseSerializer
    filter_fields = CoreModels.get_fields(CoreModels.FruitUse)
    filter_backends = (filters.DjangoFilterBackend, filters.OrderingFilter)

class LocationViewSet(viewsets.ModelViewSet):
    queryset = CoreModels.Location.objects.all()
    serializer_class = CoreSerializers.LocationSerializer
    filter_fields = CoreModels.get_fields(CoreModels.Location)
    filter_backends = (filters.DjangoFilterBackend, filters.OrderingFilter)

class RootstockViewSet(viewsets.ModelViewSet):
    queryset = CoreModels.Rootstock.objects.all()
    serializer_class = CoreSerializers.RootstockSerializer
    filter_fields = CoreModels.get_fields(CoreModels.Rootstock)
    filter_backends = (filters.DjangoFilterBackend, filters.OrderingFilter)

