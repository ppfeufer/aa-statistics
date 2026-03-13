from django.contrib import admin

from .models import StatsCharacter, zKillMonth, zKillStatsFilter

admin.site.register(StatsCharacter)


@admin.register(zKillMonth)
class zKillMonthAdmin(admin.ModelAdmin):
    list_display = ('char', 'year', 'month', 'last_update')
    search_fields = ['char__character__character_name']
    ordering = ('char', '-year', 'month')


@admin.register(zKillStatsFilter)
class zKillStatsFilterAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'kill_count', 'months']
