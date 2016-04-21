from django.contrib import admin
from django.conf.urls import patterns
from django.shortcuts import  render_to_response
from django.template import RequestContext
import labels.models as LabelModels



class LabelInline(admin.StackedInline):
    model = LabelModels.LabelEntry
    extra = 5
    ordering = ('cultivar',)

    def formfield_for_dbfield(self, db_field, **kwargs):
        formfield = super(LabelInline, self).formfield_for_dbfield(db_field, **kwargs)
        if db_field.name == 'cultivar':
            formfield.choices = formfield.choices
        return formfield

class OrderAdmin(admin.ModelAdmin):
    inlines =[LabelInline,]




admin.site.register(LabelModels.NurseryLabelOrder, OrderAdmin)
