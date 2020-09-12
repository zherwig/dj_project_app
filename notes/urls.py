from django.urls import path
from notes import views as note_views

# Needed for reverse lookup and dynamic links
app_name = 'notes'

urlpatterns = [
    path('', note_views.notes_list_view, name='note_list_view'),
    path('create/', note_views.note_create_view, name='note_create_view'),
    path('create/project/<int:projectid>/', note_views.note_create_view, name='note_create_view'),
    path('create/task/<int:taskid>/', note_views.note_create_view, name='note_create_view'),
    path('create/action/<int:actionid>/', note_views.note_create_view, name='note_create_view'),
    path('<int:id>/', note_views.note_detail_view, name='note_detail_view'),
    path('<int:id>/update/', note_views.note_update_view, name='note_update_view'),
    path('<int:id>/delete/', note_views.note_delete_view, name='note_delete_view'),    
]
