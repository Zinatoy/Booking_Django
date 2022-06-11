from django import forms 
from apps.contact.models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact 
        fields = ('name','lastname', 'phone', 'email','message')
        widgets = {
            'name' : forms.TextInput(attrs={'class': "form-control"}),
            'lastname' : forms.TextInput(attrs={'class': "form-control"}),
            'phone' : forms.TextInput(attrs={'class': "form-control"}),
            'email' : forms.EmailInput(attrs={'class': "form-control"}),
            'message' : forms.TextInput(attrs={'class': "form-control"}), 
        }