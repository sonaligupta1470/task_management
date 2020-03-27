from django import forms
from .models import Task
from django.contrib.auth.models import User


class TaskModelForm(forms.ModelForm):

    class Meta:
        model = Task
        assigned_to = forms.ModelMultipleChoiceField(queryset=User.objects.all(), widget=forms.CheckboxSelectMultiple )
        fields = ['task_name', 'description', 'status', 'assigned_to']

    def __init__(self, *args, **kwargs):
        super(TaskModelForm, self).__init__(*args, **kwargs)
        print(User.objects.all())
        # self.fields['assigned_to'].widget = forms.CheckboxSelectMultiple()

class CommentForm(forms.Form):
    comment = forms.CharField(max_length=220)



