from ast import Pass
from django.contrib import admin
from .models import HubModels
class HubAdmin(admin.ModelAdmin):
    pass

admin.site.register(HubModels , HubAdmin)