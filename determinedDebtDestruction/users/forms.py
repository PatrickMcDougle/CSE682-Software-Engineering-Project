from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    
    #This extends the UserCreationForm and tells it to save to the User database entry
    # The fields indicate the order in which information is requested from the user
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    
    #This extends the UserCreationForm and tells it to save to the User database entry
    # The fields indicate the order in which information is requested from the user
    class Meta:
        model = User
        fields = ['username', 'email']