from django.urls import path
from projects import views as projects_views

# Needed for reverse lookup and dynamic links
app_name = 'projects'

urlpatterns = [
    path('', projects_views.projects_list_view, name='projects_list_view'),
    path('create/', projects_views.project_create_view, name='project_create_view'),
    path('<int:id>/', projects_views.project_detail_view, name='project_detail_view'),
    path('<int:id>/update/', projects_views.project_update_view, name='project_update_view'),
    path('<int:id>/delete/', projects_views.project_delete_view, name='project_delete_view'),    
]
