from django.contrib import admin

from .models import DetailsModel, PressComModel

class DetailsAdmin(admin.ModelAdmin):
    pass

admin.site.register(DetailsModel, DetailsAdmin)
admin.site.register(PressComModel)
