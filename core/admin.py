# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Conference, Division, Team


@admin.register(Conference)
class ConferenceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'nhl_id')
    search_fields = ('name',)


@admin.register(Division)
class DivisionAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'nhl_id',
        'conference',
        'nameshort',
        'abbreviation',
    )
    list_filter = ('conference',)
    search_fields = ('name',)


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'nhl_id',
        'venue',
        'city',
        'locationName',
        'division',
        'teamName',
        'abbreviation',
        'officialSiteUrl',
    )
    list_filter = ('division',)
    search_fields = ('name',)