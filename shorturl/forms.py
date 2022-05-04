from django import forms

from .models import URL


class ChooseURLNameForm(forms.ModelForm):
    class Meta:
        model = URL
        fields = ['url_long', 'url_custom']


class HashURLNameForm(forms.ModelForm):
    class Meta:
        model = URL
        fields = ['url_long']
