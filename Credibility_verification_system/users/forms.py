from django import forms
from django.contrib.auth.forms import UserCreationForm , UserChangeForm,PasswordChangeForm
from django.contrib.auth.hashers import make_password
from .models import CustomUser

class UserForm(UserCreationForm):
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'type': 'password',
        'data-toggle': 'password',
        'id': 'password1',
        'onfocus': 'this.type="password"',
        }),
    )
    password2 = forms.CharField(
        label="Retype Password",
        widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'type': 'password',
        'data-toggle': 'password',
        'id': 'password2',
        'onfocus': 'this.type="password"',
        }),
    )

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name','gender','country' ,'username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(UserForm, self).save(commit=False)
        user.password = make_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user

class StatementForm(forms.Form):
    statement = forms.CharField(
        label="Statement",
        widget=forms.Textarea(attrs={'rows': 4}),
        help_text="Enter your statement here. Note: The model might display an inaccurate verdict to a statement, so please double check the Verdict it provides.")


class EditProfileForm(UserChangeForm):
    class Meta:
        model = CustomUser 
        fields = ['first_name','last_name','username', 'email', 'password'] 
        
        
class ChangePasswordForm(PasswordChangeForm):
    pass


class OTPForm(forms.Form):
    otp = forms.CharField(
        max_length=6,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=True
    )