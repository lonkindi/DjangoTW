from django.contrib import admin

from hzapi.models import Anket


@admin.register(Anket)
class AnketAdmin(admin.ModelAdmin):
    pass
