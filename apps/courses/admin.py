from django.contrib import admin
from .models import Course, Lesson, Video, CourseResource


class CourseAdmin(admin.ModelAdmin):
    list_display = ('name',)


class LessonAdmin(admin.ModelAdmin):
    list_display = ('name',)


class VideoAdmin(admin.ModelAdmin):
    list_display = ('name',)


class ResourceAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(CourseResource, ResourceAdmin)
