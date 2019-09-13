from django.contrib.auth.models import User
from django.contrib.auth.foms import UserCreationForm
from django import forms

class SignUpForm(UserCreationForm):
    email = (max_length = 254, help_text = 'Required, enter a valid email address')
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
