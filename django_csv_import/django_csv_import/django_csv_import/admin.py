from django.contrib import admin

# Register your models here.

from django_csv_import.django_csv_import.models import Album
from django_csv_import.django_csv_import.models import Musician
from django_csv_import.django_csv_import.models import Person

class AlbumAdmin(admin.ModelAdmin):
    pass

class MusicianAdmin(admin.ModelAdmin):
    pass

class PersonAdmin(admin.ModelAdmin):
    pass

admin.site.register(Album, AlbumAdmin)
admin.site.register(Musician, MusicianAdmin)
admin.site.register(Person, PersonAdmin)
