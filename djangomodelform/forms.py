from django import forms
from .models import Granth


class BookModelForm(forms.ModelForm):
    class Meta:
        model = Granth
        fields = "__all__"