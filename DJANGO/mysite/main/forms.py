from django import forms

class CreateNewList(forms.Form):
    name=forms.CharField(label ="NAME",max_length="200")

    