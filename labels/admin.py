from django.contrib import admin
from django.conf.urls import patterns
from django.shortcuts import  render_to_response
from django.template import RequestContext
import labels.models as LabelModels



class LabelInline(admin.StackedInline):
    model = LabelModels.LabelEntry
    extra = 5
    ordering = ('cultivar',)

class OrderAdmin(admin.ModelAdmin):
    inlines =[LabelInline,]


admin.site.register(LabelModels.NurseryLabelOrder, OrderAdmin)
