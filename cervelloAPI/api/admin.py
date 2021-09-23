from django.contrib import admin
from api.models import Section, Lectures, Course
from import_export.admin import ImportExportModelAdmin

admin.site.register(Course)
admin.site.register(Section)
admin.site.register(Lectures)

class CourseAdmin(ImportExportModelAdmin):
    list_display = ("title")
