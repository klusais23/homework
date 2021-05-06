from django import forms
from visit.models import Visit


class VisitForm(forms.ModelForm):
    class Meta:
        model = Visit
        fields = [
            'user',
            'email',
        ]