from django.contrib import admin
import market.models as MarketModels


class MarketInventoryInLine(admin.StackedInline):
    model = MarketModels.MarketInventoryEntry
    extra = 5

class MarketInventoryAdmin(admin.ModelAdmin):
    inlines = [MarketInventoryInLine,]


admin.site.register(MarketModels.MarketInventoryEntry)
admin.site.register(MarketModels.MarketInventory, MarketInventoryAdmin)

