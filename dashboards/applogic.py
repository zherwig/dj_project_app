from topics.models import Topic
from projects.models import Project
from tasks.models import Task
from actions.models import Action
from django.contrib.auth.models import User
import datetime
from django.utils import timezone

def get_topics_with_projects_and_open_tasks():
    #Getting all topics and related projects
    all_topics = Topic.objects.filter(completed = False).order_by('title')
    topic_list = [
        {'topic': topic, 
        'projects': Project.objects
                            .filter(topic = topic.id)
                            .filter(closed = False)
                            .order_by('title')
        } 
        for topic in all_topics]
    
    for element in topic_list:
        for element_project in element['projects']:
            element_project.tasks = Task.objects.filter(project = element_project.id, completed = False).order_by('duedate')
            for task in element_project.tasks:
                if task.duedate:
                    if task.duedate <  datetime.date.today() + datetime.timedelta(days=7):
                        task.due = True
                else:
                    task.due = False
        
    return topic_list

def get_completed_tasks():
    all_tasks = Task.objects.filter(
                completed = True,
                completed_at__gte = datetime.datetime.now(tz=timezone.utc) - datetime.timedelta(days=7)
            ).order_by('duedate')
    return [task for task in all_tasks if task.project.excludeFromReports == False and task.excludeFromReports == False]


def get_actions_per_date_range(start_day_number, end_day_number):
    start_range = datetime.date.today() + datetime.timedelta(days=start_day_number)
    end_range = datetime.date.today() + datetime.timedelta(days=end_day_number)
    return Action.objects.filter(duedate__range=[start_range, end_range], completed=False)

def get_staff_actions_per_date_range(start_day_number, end_day_number, staff_member):
    staff_member_id = User.objects.get(username__contains=staff_member)
    start_range = datetime.date.today() + datetime.timedelta(days=start_day_number)
    end_range = datetime.date.today() + datetime.timedelta(days=end_day_number)
    return Action.objects.filter(duedate__range=[start_range, end_range], completed=False, assignee=staff_member_id)

def get_staff_open_tasks(staff_member):
    return [
        {
            'name': "Overdue",
            'tasks': get_staff_actions_per_date_range(-900, -1, staff_member)
        },
        {
            'name': "Today",
            'tasks': get_staff_actions_per_date_range(0, 0, staff_member)
        },
        {
            'name': "Future",
            'tasks': get_staff_actions_per_date_range(1, 1000, staff_member)
        },
    ]

def move_action_to_today(action_id):
    action_to_update = Action.objects.filter(id = action_id)[0]
    if action_to_update:
        action_to_update.duedate = datetime.date.today()
        action_to_update.save()