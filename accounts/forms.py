from django import forms
from .models import Profile
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Foydalanuvchi ismini kiriting'}),
                               help_text="<small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small>")
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control','placeholder':'Email manzilingizni kiriting'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ismingizni kiriting'}))
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Familiyangizni kiriting'}))
    password1 = forms.CharField(label="Password",widget=forms.PasswordInput(attrs={'class':'form-control'}),
                                    help_text="<small><ul><li>Siznining parolingiz boshqa malumotlar bilan bircil bo'lmasligi kerak.</li>\
                                    <li>Sizning parolingiz 8 ta belgidan ko'p bo'lsin</li>\
                                    <li>Your password can't be a commonly used password.</li>\
                                    <li>Your password can't be entirely numeric.</li></ul></small>")
    password2 = forms.CharField(label="Password confirmation", widget=forms.PasswordInput(attrs={'class': 'form-control'}),\
                                help_text="<small>Parolni tasdiqlash uchun qaytadan kiriting</small>")
    class Meta:
        model = User
        fields=['username','email','first_name','last_name','password1', 'password2',]
