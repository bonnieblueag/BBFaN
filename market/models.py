from django.db import models
from django.contrib.auth.models import User
from core import models as CoreModels


class MarketInventoryEntry(CoreModels.BaseModel):
    grafted_tree = models.ForeignKey(CoreModels.GraftedStock, null=True, blank=True)
    seedling_tree = models.ForeignKey(CoreModels.SeedlingTree, null=True, blank=True)
    count = models.PositiveIntegerField()
    inventory = models.ForeignKey('MarketInventory')


class MarketInventory(CoreModels.BaseModel):
    user = models.ForeignKey(User)
    market_date = models.DateTimeField()


