from django import forms
from .models import AbsenceForm
from .models import AbsenceReview
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class AbsenceFormForm(forms.ModelForm):
    class Meta:
        model = AbsenceForm
        fields = ['reason']

class AbsenceReviewForm(forms.ModelForm):
    class Meta:
        model = AbsenceReview
        fields = ['decision', 'feedback']
        widgets = {
            'feedback': forms.Textarea(attrs={'rows': 4})
        }

class StudentSignupForm(UserCreationForm):
    student_id = forms.CharField(max_length=20)
    name = forms.CharField(max_length=100)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'student_id', 'name', 'email']