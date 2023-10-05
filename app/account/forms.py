from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from django import forms


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('email',)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('email',)


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=100, widget=forms.PasswordInput, label='Repeat password')

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email','password']

    def clean_email(self):
        data = self.cleaned_data['email']
        if CustomUser.objects.filter(email=data).first():
            raise forms.ValidationError('Email already in use.')
        else:
            return data

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Password don\'t match')
        else:
            return cd['password2']