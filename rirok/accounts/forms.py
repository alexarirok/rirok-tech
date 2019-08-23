from django import forms 
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth import get_user_model

User = get_user_model() 

class SignupForm(UserCreationForm):
    firstname = forms.CharField(max_length = 30, required=False, help_text='optional')
    lastname = forms.CharField(max_length = 30, required=False, help_text='optional')
    email = forms.EmailField(max_length = 100, help_text = 'required')

    class meta:
        model = User 
        fields = ['username', 'firstname', 'lastname', 'email', 'password1', 'password2']