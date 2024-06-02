from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User
from .models import *

class SignupForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
            
        

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)





class AddComapnyForm(forms.ModelForm):

    class Meta:
        model = Company
        fields =['name']
        





class AddDepatmentForm(forms.ModelForm):

    class Meta:
        model = Department
        fields =['company','name',]
        

class AddEmployeeForm(forms.ModelForm):
    
    class Meta:
        model = Employee
        fields =['company','department','name','email','mobile_number','address','designation']



class EditEmployeeForm(forms.Form):
    
    name = forms.CharField(max_length=255,required=False)
    email = forms.EmailField(required=False)
    mobile_number = forms.CharField(max_length=11,required=False)
    address = forms.CharField(required=False)
    
