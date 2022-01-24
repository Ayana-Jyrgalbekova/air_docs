from django.contrib import admin

from core.models import *


class DocAdmin(admin.ModelAdmin):
    list_display = ("fio", "category", "text",)


admin.site.register(Categories)
admin.site.register(Client)
admin.site.register(Documents, DocAdmin)
