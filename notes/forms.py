from django import forms
from .models import Note
from crispy_forms.helper import FormHelper
from crispy_forms.layout import HTML, Div, Field, Layout, Submit

class NoteCreationForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit'))
    
    class Meta:
        model = Note
        fields = '__all__'

class AddNoteForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['note_text'].widget = forms.Textarea(attrs={'rows': 6, 'cols': 25})
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submitnote', 'Submit'))
        self.helper.layout = Layout(
            Div(
                Div( 
                    Field('note_title'),
                    Field('note_text'),
                    Field('highlighted')
                ), css_class='note_submission_form_div'
            )
        )
    
    class Meta:
        model = Note
        fields = ('note_title', 'note_text', 'highlighted')
