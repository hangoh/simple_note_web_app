from django.urls import path
from notes import views
app_name='notes'

urlpatterns=[
    path('mynotes',views.main_page ,name='mynotes'),
    path('create_notelist/',views.create_notelist,name='create_notelist'),
    path('notes_page/remove_notelist/<name_id>/',views.remove_notelist,name='remove_notelist'),
    path('notes_page/<name_id>/',views.notes_page,name='notes_page'),
    path('notes_page/<name_id>/create_note/',views.create_note,name='create_note'),
    path('notes_page/<name_id>/remove_note/<note_id>/',views.remove_note,name='remove_note'),
    path('notes_page/<name_id>/<note_id>/',views.notes_detail,name='notes_detail'),
]