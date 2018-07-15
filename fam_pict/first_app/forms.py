from django import forms
from first_app.models import SignUp
from first_app.models import UserProfileInfo
from django.contrib.auth.models import User

class NewUserForm(forms.ModelForm):
    class Meta():
        model = SignUp
        fields = '__all__'

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'email', 'password')

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('website', 'profile_pic')
