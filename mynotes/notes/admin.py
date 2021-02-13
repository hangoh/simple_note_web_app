from django.contrib import admin
from notes.models import NotesList,Notes
# Register your models here.

class NotesListAdmin(admin.ModelAdmin):
    list_display=['user','name','id']
    search_fields=['user','name']
    list_filter=['user']
    readonly_fields=['user','name','id']

admin.site.register(NotesList,NotesListAdmin)
class NotesAdmin(admin.ModelAdmin):
    list_display=['title','under_notelist','id']
    search_fields=['title','under_notelist']
    list_filter=['title','under_notelist']
    readonly_fields=['title','under_notelist','id']

admin.site.register(Notes,NotesAdmin)