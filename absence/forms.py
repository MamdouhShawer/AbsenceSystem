from django import forms
from .models import AbsenceForm

class AbsenceFormForm(forms.ModelForm):
    class Meta:
        model = AbsenceForm
        fields = ['reason']
