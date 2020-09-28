from tasks.models import Task
from actions.models import Action
import datetime

def get_tasks_and_open_and_closed_actions(projectid):
    all_open_tasks = Task.objects.filter(project_id = projectid).filter(completed=False).order_by('duedate') 
    for task in all_open_tasks:
        task.openactions = Action.objects.filter(task = task.id, completed = False).order_by('duedate')
    
    return all_open_tasks