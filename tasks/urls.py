from django.urls import path
from tasks import views as task_views

# Needed for reverse lookup and dynamic links
app_name = 'tasks'

urlpatterns = [
    path('', task_views.tasks_list_view, name='task_list_view'),
    path('create/', task_views.task_create_view, name='task_create_view'),
    path('create/<int:projectid>/', task_views.task_create_view, name='task_create_view_with_project'),
    path('<int:id>/', task_views.task_detail_view, name='task_detail_view'),
    path('<int:id>/update/', task_views.task_update_view, name='task_update_view'),
    path('<int:id>/updateprogress/', task_views.task_update_progress_view, name='task_update_progress_view'),
    path('<int:id>/delete/', task_views.task_delete_view, name='task_delete_view'),
    path('<int:id>/complete/', task_views.task_complete_view, name='task_complete_view'),    
]
