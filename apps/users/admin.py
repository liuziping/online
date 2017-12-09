from django.contrib import admin
from .models import UserProfile, EmailVerifyRecord, Banner


class UsersAdmin(admin.ModelAdmin):
    list_display = ('username', 'password', 'email', 'is_active', 'is_staff', 'is_superuser')


class EmailAdmin(admin.ModelAdmin):
    list_display = ('code', 'email', 'send_type','send_time')


class BannerAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'url', 'index', 'add_time')


admin.site.register(UserProfile, UsersAdmin)
admin.site.register(EmailVerifyRecord, EmailAdmin)
admin.site.register(Banner, BannerAdmin)