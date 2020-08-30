from django import forms
from .models import Project
from django.contrib.auth.models import User
import datetime

class ProjectCreationForm(forms.ModelForm):
    title = forms.CharField(required=True, widget=forms.TextInput(
        attrs={
            'placeholder' : "The project Title",
            'class': "form-control",
            'id': 'title_form_field'
    }))
    class Meta:
            model = Project
            fields = '__all__'
    
    #Format here is: def clean_<fieldname>(self, *args, **kwargs)
    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get("title")
        if "CFE" in title:
            return title
        else:
            raise forms.ValidationError("This is not a valid title")


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