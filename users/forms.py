from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth.models import User
from messeneger.bulma_mixin import BulmaMixin


class SignUpForm(BulmaMixin, UserCreationForm):
    username = forms.CharField()
    email = forms.EmailField()
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Username is already taken.")
        return username


# class SignUpForm(BulmaMixin, UserCreationForm):
#     username = forms.CharField()

#     email = forms.CharField()

#     password1 = forms.PasswordInput()

#     password2 = forms.PasswordInput()

#     class Meta:
#         model = User
#         fields = ('username', 'email', 'password1', 'password2')


class SignInForm(BulmaMixin, AuthenticationForm):
    username = forms.CharField()
    password = forms.PasswordInput()

    class Meta:
        model = User
        fields = ['username', 'password']


class EditProfileForm(BulmaMixin, forms.ModelForm):
    first_name = forms.CharField(label='First name')
    last_name = forms.CharField(label='Last name')
    username = forms.CharField(label='Username')
    email = forms.CharField(label='Email address')

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email')


class ResetPasswordForm(BulmaMixin, PasswordChangeForm):
    old_password = forms.CharField(
        widget=forms.PasswordInput(),
        label='Old password',
    )
    new_password1 = forms.CharField(
        widget=forms.PasswordInput(),
        label='New password',
    )
    new_password2 = forms.CharField(
        widget=forms.PasswordInput(),
        label='Repeat new password'
    )

    class Meta:
        model = User
        fields = ['old_password', 'new_password1', 'new_password2']








