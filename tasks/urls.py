from django.urls import path
from tasks import views as task_views

# Needed for reverse lookup and dynamic links
app_name = 'tasks'

urlpatterns = [
    path('', task_views.TaskListView.as_view(), name='task_list_view'),
    # path('create/', projects_views.project_create_view, name='project_create_view'),
    path('<int:id>/', task_views.TaskDetailView.as_view(), name='task_detail_view'),
    # path('<int:id>/update/', projects_views.project_update_view, name='project_update_view'),
    # path('<int:id>/delete/', projects_views.project_delete_view, name='project_delete_view'),    
]
