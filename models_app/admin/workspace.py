from django.contrib import admin
from django.contrib.admin.widgets import FilteredSelectMultiple
from django import forms

from models_app.models import UserWorkspace, User
from models_app.models.workspace.models import Workspace


class WorkspaceUsersForm(forms.ModelForm):
    class Meta:
        model = Workspace
        exclude = []

    users = forms.ModelMultipleChoiceField(
        queryset=User.objects.all(),
        required=False,
        widget=FilteredSelectMultiple('Пользователи', is_stacked=False),
    )


@admin.register(Workspace)
class WorkspaceAdmin(admin.ModelAdmin):
    form = WorkspaceUsersForm
