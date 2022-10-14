from django.contrib import admin
from webapp.models import Task, Type, Status
# Register your models here.


class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'summary', 'description', 'status')
    list_filter = ('status', )
    fields = ('id', 'summary', 'description', 'type', 'status')
    readonly_fields = ('id',)


admin.site.register(Task, TaskAdmin)


class TypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


admin.site.register(Type, TypeAdmin)


class StatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


admin.site.register(Status, StatusAdmin)
