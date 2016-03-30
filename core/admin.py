from django.contrib import admin
from core import models as CoreModels


admin.site.register(CoreModels.Rootstock)
admin.site.register(CoreModels.Cultivar)
admin.site.register(CoreModels.FruitUse)
admin.site.register(CoreModels.GraftedStock)
admin.site.register(CoreModels.Location)
admin.site.register(CoreModels.Pot)
admin.site.register(CoreModels.RootstockInventory)
admin.site.register(CoreModels.Scion)
admin.site.register(CoreModels.ScionSource)
admin.site.register(CoreModels.SeedlingInfo)
admin.site.register(CoreModels.SeedlingTree)
admin.site.register(CoreModels.Species)

