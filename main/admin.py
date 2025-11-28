from django.contrib import admin
from django.contrib.auth.models import Group, User

from .models import *


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Season)
class SeasonAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Club)
class ClubAdmin(admin.ModelAdmin):
    list_display = ('name', 'logo', 'president', 'coach', 'found_date', 'country',)
    list_filter = ('country',)
    search_fields = ('name', 'president', 'coach')


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('name', 'number', 'position', 'birth_date', 'price', 'country',)
    list_filter = ('country', 'club', 'position', 'number')
    search_fields = ('name',)


@admin.register(Transfer)
class TransferAdmin(admin.ModelAdmin):
    list_display = ('player', 'old_club', 'new_club', 'price', 'price_tft', 'created_at', 'season',)
    list_filter = ('player', 'season', 'old_club', 'new_club', 'season')
    ordering = ('-price',)


admin.site.unregister(User)
admin.site.unregister(Group)