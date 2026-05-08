from django.contrib import admin
from .models import Buket

@admin.register(Buket)
class BuketAdmin(admin.ModelAdmin):
    list_display = ['ime', 'tip_na_cveke', 'golemina', 'cena', 'sveze', 'dali_e_od_EU']
    list_filter = ['golemina', 'sveze', 'dali_e_od_EU']
    search_fields = ['ime', 'tip_na_cveke']