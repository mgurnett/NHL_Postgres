# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Conference, Division, Team, Player, Player_vitals


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
    search_fields = ('name',)


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'fullName',
        'nhl_id',
        'jerseyNumber',
        'position_name',
        'position_type',
        'position_ab',
        'team',
    )


@admin.register(Player_vitals)
class Player_vitalsAdmin(admin.ModelAdmin):
    list_display = (
        'player',
        'firstName',
        'lastName',
        'birthDate',
        'birthCity',
        'birthCountry',
        'nationality',
        'height',
        'weight',
        'active',
        'alternateCaptain',
        'captain',
        'rookie',
        'shootsCatches',
        'rosterStatus',
    )
    list_filter = (
        'player',
        'birthDate',
        'active',
        'alternateCaptain',
        'captain',
        'rookie',
    )