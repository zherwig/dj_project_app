from django.urls import path
from actions import views as action_views

# Needed for reverse lookup and dynamic links
app_name = 'actions'

urlpatterns = [
    path('', action_views.actions_list_view, name='action_list_view'),
    path('create/', action_views.action_create_view, name='action_create_view'),
    path('create/<int:projectid>/', action_views.action_create_view, name='action_create_view'),
    path('create/<int:projectid>/<int:taskid>/', action_views.action_create_view, name='action_create_view'),
    path('create/<int:projectid>/<int:taskid>/<str:assignee>', action_views.action_create_view, name='action_create_view'),
    path('<int:id>/', action_views.action_detail_view, name='action_detail_view'),
    path('<int:id>/update/', action_views.action_update_view, name='action_update_view'),
    path('<int:id>/delete/', action_views.action_delete_view, name='action_delete_view'),    
    path('<int:id>/complete/', action_views.action_complete_view, name='action_complete_view'),
    path('<int:id>/completeandnext/', action_views.action_complete_and_next_view, name='action_complete_and_next_view'),
    path('<int:id>/togglehighlight/', action_views.action_highlight_toggle_view, name='action_highlight_toggle_view'),
    path('<int:id>/push/', action_views.action_delay_by_a_day_view, name='action_delay_by_a_day_view'),
        
]
