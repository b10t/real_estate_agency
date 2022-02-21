from django.contrib import admin

from .models import Flat, Claim


@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    list_display = ('address',
                    'price',
                    'new_building',
                    'construction_year',
                    'town'
                    )
    list_editable = ['new_building']
    list_filter = ['new_building']
    readonly_fields = ['created_at']
    search_fields = ('town', 'address', 'owner')
    raw_id_fields = ['liked_by']


@admin.register(Claim)
class ClaimAdmin(admin.ModelAdmin):
    list_display = ('user',
                    'flat',
                    'description'
                    )
    raw_id_fields = ('user', 'flat')
