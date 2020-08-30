from django.urls import path
from tasks import views as task_views

# Needed for reverse lookup and dynamic links
app_name = 'tasks'

urlpatterns = [
    path('', task_views.TaskListView.as_view(), name='task_list_view'),
    path('create/', task_views.TaskCreateView.as_view(), name='task_create_view'),
    path('<int:id>/', task_views.TaskDetailView.as_view(), name='task_detail_view'),
    path('<int:id>/update/', task_views.TaskUpdateView.as_view(), name='task_update_view'),
    path('<int:id>/delete/', task_views.TaskDeleteView.as_view(), name='task_delete_view'),    
]
