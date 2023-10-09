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
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')

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
        help_text="Enter your statement here."
    )
    originator = forms.CharField(
        label="Statement Originator",
        max_length=100,
        help_text="Enter the originator of the statement."
    )
    source = forms.CharField(
        label="Statement Source",
        max_length=100,
        help_text="Enter the source of the statement."
    )
    statement_date = forms.DateField(
        label="Statement Date",
        help_text="Enter the date of the statement",
        widget=forms.DateInput(attrs={'type': 'date'})
    )


class EditProfileForm(UserChangeForm):
    class Meta:
        model = CustomUser 
        fields = ['first_name','last_name','username', 'email', 'password'] 
        
        
class ChangePasswordForm(PasswordChangeForm):
    pass