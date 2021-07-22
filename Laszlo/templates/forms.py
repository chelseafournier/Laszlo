from django import forms

from .models import ContactMe

class CutenessForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Name"}))
    email = forms.EmailField(widget=forms.TextInput(attrs={"placeholder": "Email"}))
    phone_number = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "(###) ###-####"}))
    description = forms.CharField(widget=forms.Textarea(attrs={"placeholder": "Please describe the nature of your request"}))

    class Meta:
        fields = [
            'name',
            'email',
            'phone_number',
            'description'
        ]
        model = ContactMe
