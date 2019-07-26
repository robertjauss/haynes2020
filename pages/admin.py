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


@admin.register(NewsArticle)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publish_date')
    prepopulated_fields = {"slug": ("title",)}


@admin.register(CarouselImage)
class CarouselAdmin(admin.ModelAdmin):
    list_display = ('image', 'active')


@admin.register(Speech)
class SpeechAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publish_date')
    prepopulated_fields = {'slug': ('title',)}
