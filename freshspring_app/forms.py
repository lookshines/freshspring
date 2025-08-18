from django import forms
from .models import ContactMessages, Comment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group

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
        
class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ['name','email','message']
        
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write your mesaage'}),     
        }
        
        labels= {
            'name': '', 
            'email': '', 
            'message': ''
        }
        
#class UserRegistrationForm(UserCreationForm):
 #   group = forms.ModelChoiceField(
  #      queryset=Group.objects.all(),
   #     required=True,
    #    widget=forms.Select(attrs={'class': 'form-select form-control'}),
     #   label='Group',
      #  help_text='Select the group for the user.'
    #)
    
    #class Meta(UserCreationForm.Meta):
     #   model = User
      #  fields = ('username', 'email', 'group', 'is_staff', 'is_active')
        
    #def save(self, commit=True):
     #   user = super().save(commit=False)
      #  if commit:
       #     user.save()
            # clear groups first then add only the selected one
        #    user.groups.clear()
         #   user.groups.add(self.cleaned_data['group'])
        #return user