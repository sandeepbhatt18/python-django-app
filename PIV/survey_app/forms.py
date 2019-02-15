from django import forms
from survey_app.models import survey
from django.contrib.auth.models import User
from .models import UserProfileInfo

class NewSurvey(forms.ModelForm):

    class Meta():
        model = survey
        fields = '__all__'

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')


class UserProfileInfoForm(forms.ModelForm):

    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site',)
