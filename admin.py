from django.contrib import admin
from .models import *
class PracownikAdmin(admin.ModelAdmin):
    search_fields = ['nazwisko_imie','nr_pracownika']

# Register your models here.
admin.site.register(Potwierdz)
admin.site.register(Szablon)
admin.site.register(Narzedzie)
admin.site.register(Pobranie)
admin.site.register(PobranieOdziez)
admin.site.register(Pracownik,PracownikAdmin)
admin.site.register(Odziez)
admin.site.register(SzablonOdziez)
