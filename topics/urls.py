from django.urls import path
from topics import views as topic_views

# Needed for reverse lookup and dynamic links
app_name = 'topics'

urlpatterns = [
    path('', topic_views.topics_list_view, name='topic_list_view'),
    path('create/', topic_views.topic_create_view, name='topic_create_view'),
    path('<int:id>/', topic_views.topic_detail_view, name='topic_detail_view'),
    path('<int:id>/update/', topic_views.topic_update_view, name='topic_update_view'),
    path('<int:id>/delete/', topic_views.topic_delete_view, name='topic_delete_view'),    
]
