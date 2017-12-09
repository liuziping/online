from django.contrib import admin
from .models import  UserMessage


class MsgAdmin(admin.ModelAdmin):
    list_display = ('user', 'message')


admin.site.register(UserMessage, MsgAdmin)
