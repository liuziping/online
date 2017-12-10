from django.contrib import admin
from .models import UserMessage, UserCourse, CourseComments, UserFavorite


class MsgAdmin(admin.ModelAdmin):
    list_display = ('user', 'message')


class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('user',)


class CourseAdmin(admin.ModelAdmin):
    list_display = ('user',)


class CommentsAdmin(admin.ModelAdmin):
    list_display = ('user',)


admin.site.register(UserMessage, MsgAdmin)
admin.site.register(UserFavorite, FavoriteAdmin)
admin.site.register(CourseComments, CommentsAdmin)
admin.site.register(UserCourse, CourseAdmin)
