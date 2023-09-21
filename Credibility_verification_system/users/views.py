from django.shortcuts import render,redirect
from .forms import UserForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
 
# Create your views here.
def home(request):
    return render(request,'users/home.html')


def register(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Hi {username}, your account was created successfully')
            return redirect('login')
    else:
        form = UserForm()
    return render(request,'users/register.html',{'form': form})

@login_required()
def profile(request):
    return render(request, 'users/profile.html')

def login(request):
    if request.user.is_authenticated:
        return redirect('profile')  # Redirect to the profile page if the user is already logged in
    return render(request, 'users/login.html')