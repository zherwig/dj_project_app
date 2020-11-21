from topics.models import Topic
from projects.models import Project
from tasks.models import Task
from actions.models import Action
import datetime

def get_topics_with_projects_and_open_tasks():
    #Getting all topics and related projects
    all_topics = Topic.objects.all().order_by('title')
    topic_list = [
        {'topic': topic, 
        'projects': Project.objects
                            .filter(topic = topic.id)
                            .filter(closed = False)
                            .order_by('title')
        } 
        for topic in all_topics]

    #determining latest due date for use in GUi and sorting
    for element in topic_list:
    #     try:
    #         element['top_due_date'] = element['projects'][0].duedate
    #     except IndexError:
    #         element['top_due_date'] = datetime.date.today()
    #     #adding related tasks 
        for element_project in element['projects']:
            element_project.tasks = Task.objects.filter(project = element_project.id, completed = False).order_by('duedate')
    
    # topic_list.sort(key=lambda x: int(x['top_due_date'].strftime('%Y%m%d')))
    return topic_list

def get_actions_per_date_range(start_day_number, end_day_number):
    start_range = datetime.date.today() + datetime.timedelta(days=start_day_number)
    end_range = datetime.date.today() + datetime.timedelta(days=end_day_number)
    return Action.objects.filter(duedate__range=[start_range, end_range], completed=False)

def move_action_to_today(action_id):
    action_to_update = Action.objects.filter(id = action_id)[0]
    if action_to_update:
        action_to_update.duedate = datetime.date.today()
        action_to_update.save()