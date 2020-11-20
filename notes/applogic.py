from notes.models import Note

def getRelatedNotes(object_type, id):
    if object_type == 'project':
        notes = Note.objects.filter(project_id = id).order_by('-created_at')
    if object_type == 'task':
        notes = Note.objects.filter(task_id = id).order_by('-created_at')
    if object_type == 'action':
        notes = Note.objects.filter(action_id = id).order_by('-created_at')
    return notes
