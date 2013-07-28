from django import forms

from .models import Group


class GroupAdminForm(forms.ModelForm):
    """
    Form class for editing events in the admin interface.
    """
    is_active = forms.BooleanField(label="Is visible", required=False,
            help_text="This is used for toggling whether a group appears on the site.")
    description_markdown = forms.CharField(label="Description",
            widget=forms.Textarea(attrs={'class': 'vLargeTextField'}),
            help_text="Use <a href='http://daringfireball.net/projects/markdown/basics'>Markdown formatting</a>")

    class Meta:
        model = Group
        exclude = ('description',)
