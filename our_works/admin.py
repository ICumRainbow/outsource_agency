from django.contrib import admin

# Register your models here.
from our_works.models import Work


@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
    list_display = ['heading']
