from django import forms
from django.core.exceptions import ValidationError

from .models import URL


class ChooseURLNameForm(forms.ModelForm):
    class Meta:
        model = URL
        fields = ['url_long', 'url_custom']

    def clean_url_custom(self):
        url_custom = self.cleaned_data['url_custom']
        interdit = ['choose', 'retrieve', 'generate']
        if not url_custom:
            return url_custom

        if url_custom in interdit:
            raise ValidationError("You can't use thoses names : choose, retrieve and generate sorry!")
            # self.add_error('url_custom', 'Hello')

        return url_custom

class HashURLNameForm(forms.ModelForm):
    class Meta:
        model = URL
        fields = ['url_long']
