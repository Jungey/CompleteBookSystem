from django import forms

class DjangoForm(forms.Form):
    title = forms.CharField(max_length=50)
    author = forms.CharField(max_length=50)
    edition = forms.IntegerField()
    price = forms.IntegerField()