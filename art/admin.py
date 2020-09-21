from django.contrib import admin
from art.models import Art

class ArtAdmin(admin.ModelAdmin):
    list_display = ('name', 'content')
    list_display_links = ('name', 'content')
    search_fields = ('name', 'content')

admin.site.register(Art, ArtAdmin)
