from django import forms
from models import MiniURL

# On cree un formulaire a partir de notre modele MiniURL..
class MiniURLForm(forms.ModelForm):
    class Meta:
        model = MiniURL
        fields = ('url', 'pseudo')