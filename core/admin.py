from django.contrib import admin

from core.models import *


class DocAdmin(admin.ModelAdmin):
    list_display = ("fio", "category", "text",)


class AllDocAdmin(admin.ModelAdmin):
    list_display = ('when', 'category', 'plans')


admin.site.register(Categories)
admin.site.register(Client)
admin.site.register(Documents, DocAdmin)
admin.site.register(DocumentNames)
admin.site.register(AllDocument, AllDocAdmin)
