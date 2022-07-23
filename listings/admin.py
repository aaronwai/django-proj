from django.contrib import admin

# Register your models here.
# Listing is the class name of the models.py
from .models import Listing
# create a class for the table by passing tuple
# list_display is how data display
# list_display_links create a link selection
# filter is the filter box at the right
# list_editable for check selection, a save button will generated
# search_fields = create a search box at the top
# list_per_page ; otherwise, the list can keep going without pagation


class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published',
                    'price', 'list_date', 'realtor')
    list_display_links = ('id', 'title')
    list_filter = ('realtor',)
    list_editable = ('is_published',)
    search_fields = ('title', 'desciption', 'address',
                     'city', 'state', 'zipcode', 'price')
    list_per_page = 25


admin.site.register(Listing, ListingAdmin)
