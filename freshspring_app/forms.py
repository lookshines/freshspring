from django import forms
from .models import ContactMessages

class ContactForm(forms.ModelForm):
   
    class Meta:
        model = ContactMessages
        fields = ['fullname', 'email', 'phone', 'request', 'message']
        widgets = {
            'fullname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone'}),
            'request': forms.Select(attrs={'class': 'form-select form-control', 'placeholder': 'Select a serivce'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write your mesaage'}),     
        }
        
        labels= {
            'fullname': '', 
            'email': '', 
            'phone': '', 
            'request': '', 
            'message': ''
        }