from django import forms
from .models import Action
from crispy_forms.helper import FormHelper
from crispy_forms.layout import HTML, Div, Field, Layout, Submit
from django.shortcuts import reverse
from django.forms import HiddenInput

class ActionCreationForm(forms.ModelForm):
    previous_url = forms.URLField(required=False)

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
        # self.helper.form_action = reverse('actions:action_create_view')
        # self.fields['previous_url'].widget = HiddenInput()
        self.helper.add_input(Submit('submit', 'Submit'))

    class Meta:
        model = Action
        fields = '__all__'