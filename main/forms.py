from django import forms
from main.models import Task

class TaskForm(forms.ModelForm):
      content = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Write something here'}))
      class Meta:
            model = Task
            fields = '__all__'