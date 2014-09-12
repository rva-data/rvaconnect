from django import forms

from .models import Place


class PlaceAdminForm(forms.ModelForm):
    """
    Form class for editing places in the admin interface.
    """
    description_markdown = forms.CharField(label="Description",
            widget=forms.Textarea,
            help_text="Use <a href='http://daringfireball.net/projects/markdown/basics'>Markdown formatting</a>")

    class Meta:
        model = Place
        exclude = ('description',)

