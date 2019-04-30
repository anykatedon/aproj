from django import forms
from .models import Feedback, Doctor


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        exclude = []

class SearchDoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        exclude = []
