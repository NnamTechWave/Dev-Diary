from django import forms
from .models import blog
from .models import Comment
from ckeditor.widgets import CKEditorWidget
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm

class blogForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())


    class Meta:
        model = blog
        fields = ['title', 'content']
        db_table = "blogForm"

class AdminSignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if password != password_confirm:
            raise ValidationError("Passwords do not match")
        
        return cleaned_data

class AdminLoginForm(AuthenticationForm):
    username = forms.CharField(label='Username', max_length=254)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    error_messages = {
        'invalid_login': "",
        'inactive': "This account is inactive.",
    }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 7}),
        }

class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(
        max_length=254,
        widget=forms.TextInput(attrs={
            'class': 'form-control' 'rounded-0',
            'placeholder': 'Username',
            'id': 'username'
        })
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control' 'rounded-0',
            'placeholder': 'Password',
            'id': 'password'
        })
    )
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class EditUserForm(forms.ModelForm):
    is_staff = forms.BooleanField(required=False, label="Staff Status")
    is_superuser = forms.BooleanField(required=False, label="Admin Status")

    class Meta:
        model = User
        fields = ['first_name', 'last_name','username', 'email', 'is_staff', 'is_superuser']