from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import HTML, Div, Field, Layout, Submit

from .models import Project
from django.contrib.auth.models import User
import datetime

class ProjectCreationForm(forms.ModelForm):
    duedate = forms.DateField(
        widget=forms.TextInput(     
            attrs={'type': 'date'} 
        )
    )     
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-exampleForm'
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit'))
    
    class Meta:
            model = Project
            fields = '__all__'
    
