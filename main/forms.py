from django import forms


class AccountsForm(forms.Form):
    name = forms.CharField(label="name", max_length=100)
