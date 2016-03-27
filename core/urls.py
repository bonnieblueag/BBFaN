from django.conf.urls import include, url

from core import views as CoreViews
from rest_framework import routers

# Rest Framework
# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()

router.register(r'users', CoreViews.UserViewSet)
router.register(r'species', CoreViews.SpeciesViewSet)
router.register(r'cultivars', CoreViews.CultivarViewSet)
router.register(r'locations', CoreViews.LocationViewSet)
router.register(r'fruituses', CoreViews.FruitUseViewSet)
router.register(r'rootstocks', CoreViews.RootstockViewSet)


urls = [
    url(r'^api/species/with_cultivars/(?P<speciesID>\d+)$', CoreViews.get_species_with_cultivars,
    name='species_with_cultivars'),

]
