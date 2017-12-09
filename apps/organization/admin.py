from django.contrib import admin
from .models import CityDict, CourseOrg


class CityAdmin(admin.ModelAdmin):
    list_display = ('name',)


class OrgAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(CityDict,CityAdmin)
admin.site.register(CourseOrg, OrgAdmin)