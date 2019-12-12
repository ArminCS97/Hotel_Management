from django import forms


class CustomersForm(forms.Form):
    name = forms.CharField(max_length=255,required=True)
    surname = forms.CharField(max_length=255, required=False)

