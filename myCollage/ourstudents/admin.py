from django.contrib import admin

from ourstudents.models import Student


# Register your models here.
# admin.site.register(Student)
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'age', 'email', 'city')
    search_fields = ('id','name', 'age', 'email', 'city')
    list_filter = ('name', 'city',)
