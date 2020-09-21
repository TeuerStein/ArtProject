from .models import UserProfileInfo
from django import forms
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    ''' Form for create a username, password and email fields for User '''

    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'password', 'email')


class UserProfileInfoForm(forms.ModelForm):
    ''' Form for create a portfolio_page, portfolio_picture fields for User '''

    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_page', 'portfolio_picture')


class ChangePortfolioPictureForm(forms.ModelForm):
    ''' Form for change a portfolio picture for User '''

    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_picture',)


class ChangePortfolioPageForm(forms.ModelForm):
    ''' Form for change a portfolio page for User '''

    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_page',)


class ChangeEmailForm(forms.ModelForm):
    ''' Form for change a email for User '''

    class Meta():
        model = User
        fields = ('email',)
