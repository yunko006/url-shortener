from django import forms
from django.core.exceptions import ValidationError

from .models import URL

#https://realpython.com/django-social-forms-4/#step-10-submit-dweets-using-django-forms

class ChooseURLNameForm(forms.ModelForm):

    url_long = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(
            attrs={
                "placeholder": "Entrez un url...",
                "class": "input is-medium is-rounded",
            }
        ),
        label="",
    )
    url_custom = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(
            attrs={
                "placeholder": "Entrez un nom...",
                "class": "input is-medium is-rounded",
            }
        ),
        label="",
    )

    class Meta:
        model = URL
        fields = ['url_long', 'url_custom']

    def clean_url_custom(self):
        url_custom = self.cleaned_data['url_custom']
        interdit = ['choose', 'saved', 'generate']
        if not url_custom:
            return url_custom

        if url_custom in interdit:
            raise ValidationError("You can't use thoses names : choose, saved and generate sorry!")
            # self.add_error('url_custom', 'Hello')

        return url_custom

class HashURLNameForm(forms.ModelForm):

    url_long = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(
            attrs={
                "placeholder": "Entrez un url...",
                "class": "input is-medium is-rounded",
            }
        ),
        label="",
    )

    class Meta:
        model = URL
        fields = ['url_long']
