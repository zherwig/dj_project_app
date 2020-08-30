from django import forms
from .models import Project
from django.contrib.auth.models import User
import datetime

class ProjectCreationForm(forms.ModelForm):
    class Meta:
            model = Project
            fields = '__all__'


class RawProjectCreationForm(forms.Form):
    title = forms.CharField(required=True, widget=forms.TextInput(
        attrs={
            'placeholder' : "The project Title",
            'class': "form-control",
            'id': 'title_form_field'
    }))
    detail = forms.CharField(widget=forms.Textarea(attrs={"rows":5, "cols":20}))
    closed = forms.BooleanField(label="Completed")
    onHold = forms.BooleanField()
    priority = forms.IntegerField()
    placeInOrder = forms.IntegerField()
    duedate = forms.DateField()
    owner = forms.ModelChoiceField(queryset = User.objects.all())
    assignee = forms.ModelChoiceField(queryset = User.objects.all())
    created_at = forms.DateTimeField(initial=datetime.datetime.now(), widget=forms.HiddenInput())
    updated_at = forms.DateTimeField(initial=datetime.datetime.now())