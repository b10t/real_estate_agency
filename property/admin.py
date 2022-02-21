from django.contrib import admin

from .models import Flat, Claim, Owner


class FlatsInstanceInline(admin.TabularInline):
    model = Owner.property_apartments.through
    raw_id_fields = ('owner', 'flat')


@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    list_display = ('address',
                    'price',
                    'new_building',
                    'construction_year',
                    'town',
                    'owners_phonenumber',
                    'owner_pure_phone',
                    )
    list_editable = ['new_building']
    list_filter = ['new_building']
    readonly_fields = ['created_at']
    search_fields = ('town', 'address', 'owner')
    raw_id_fields = ['liked_by']
    inlines = [FlatsInstanceInline]


@admin.register(Claim)
class ClaimAdmin(admin.ModelAdmin):
    list_display = ('user',
                    'flat',
                    'description'
                    )
    raw_id_fields = ('user', 'flat')


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = ('owner',
                    'owners_phonenumber',
                    'owner_pure_phone',
                    )
    raw_id_fields = ['property_apartments']
    search_fields = ('owner', )
