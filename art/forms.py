from .models import Art
from django import forms


class AddArtForm(forms.ModelForm):
    ''' Form for create a new Art object '''

    class Meta():
        model = Art
        fields = '__all__'
