from django.contrib.auth.models import User
from .models import *
from django.contrib.auth.forms import UserCreationForm , forms

class UserRegistrationForm(UserCreationForm):
    first_name=forms.CharField(max_length=40)
    last_name = forms.CharField(max_length=40)
    email = forms.EmailField()

class Meta:
    model=User
    fields=[
        'username',
        'first_name',
        'last_name',
        'email',
        'password1',
        'password2',
    ]

