from django.contrib import admin

from .models import VacancyCategory, Location, Vacancy, VacancyApplication, FreelanceApplication


@admin.register(VacancyCategory)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', ]


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ['name', ]


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'on_site_option', 'remote_option', 'location', ]


@admin.register(VacancyApplication)
class VacancyApplicationAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email']


@admin.register(FreelanceApplication)
class FreelanceApplicationAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email']
