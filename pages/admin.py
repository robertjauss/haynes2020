from django.contrib import admin
from .models import *


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_start', 'date_end')


@admin.register(Volunteer)
class VolunteerAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'email', 'contacted')


@admin.register(RSVP)
class RSVPAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'email', 'contacted')
