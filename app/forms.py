"""
Definition of forms.
"""
from django.core.exceptions import ValidationError

"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class WebleadRegisterForm(forms.Form):
    membername = forms.CharField(label="membername",max_length=100)




class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=100,help_text='Required. Add a valid email address')
    username = forms.CharField(max_length=100, help_text='Required. Add a valid username')
    class Meta:
        model = User
        fields = ("username","email","password1","password2")

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        try:
            account = User.objects.get(email=email)
        except Exception as e:

            return email

        raise forms.ValidationError(f"Email is already in use.")

    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        try:
            account = User.objects.get(username=username)
        except Exception as e:
            return username
        raise forms.ValidationError(f"Username is already in use.")

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1", "")
        password2 = self.cleaned_data["password2"]
        if password1 != password2:
            raise forms.ValidationError(f"The two password fields didn't match.")
        return password2



