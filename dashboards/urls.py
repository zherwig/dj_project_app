from django.urls import path
from dashboards import views as dashboard_views

# Needed for reverse lookup and dynamic links
app_name = 'dashboards'

urlpatterns = [
    path('', dashboard_views.dashboard_list_view, name='home'),
    path('todos', dashboard_views.dashboard_actions_view, name='todos'),
    path('today', dashboard_views.dashboard_today_view, name='today'),
    path('fixoverdues', dashboard_views.dashboard_actions_fix_overdues, name='fixoverdues'),
    
]
