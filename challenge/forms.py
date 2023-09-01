from django import forms
from .models import Challenge


class ChallengeForm(forms.ModelForm):
    """
    Form for Challenge
    """
    class Meta:
        model = Challenge
        fields = ('picture', 'goal', 'link', 'review')
