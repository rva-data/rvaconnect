from django import forms

from .models import Event


class EventAdminForm(forms.ModelForm):
    """
    Form class for editing events in the admin interface.
    """
    description_markdown = forms.CharField(label="Description",
            widget=forms.Textarea,
            help_text="Use <a href='http://daringfireball.net/projects/markdown/basics'>Markdown formatting</a>")

    class Meta:
        model = Event
        exclude = ('description',)
