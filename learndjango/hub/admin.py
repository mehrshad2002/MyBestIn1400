from django.contrib import admin
from .models import HubModels

class HubAdmin(admin.ModelAdmin):
    
    fieldsets = [
        ('title' , {'fields': ['title']}),
        ('content information', {'fields': ['content' , 'author']}),
        ('image' , {'fields': ['image']}),
    ]
    search_fields = ['title']

admin.site.register(HubModels , HubAdmin)

