from projects.models import Project
from tasks.models import Task
from actions.models import Action

def get_projects_with_tasks_and_actions():
    all_projects = Project.objects.all()
    all_tasks = Task.objects.all()
    all_actions = Action.objects.all()
    print(all_projects[0])
    print(all_tasks[1].project.id)
    print(all_actions[0].task.id)
