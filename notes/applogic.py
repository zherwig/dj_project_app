from notes.models import Note

def getRelatedNotes(object_type, id):
    if object_type == 'project':
        notes = Note.objects.filter(project_id = id).order_by('-created_at')
    return notes
