from django.shortcuts import render, redirect
from .forms import UserForm, StatementForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from datetime import datetime
from django.contrib.auth import authenticate, login
import traceback


# Create your views here.
def home(request):
    return render(request, 'users/home.html')

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
    return render(request, 'users/register.html', {'form': form})

@login_required()
def user_profile(request):
    return render(request, 'users/profile.html')



def login(request):
    if request.method == 'POST':
        try:
            # Assuming you have a form for user login with 'username' and 'password' fields.
            username = request.POST['username']
            password = request.POST['password']

            # Authenticate the user
            user = authenticate(request, username=username, password=password)

            if user is not None:
                # After successful authentication, set the 'last_activity' timestamp in the session
                request.session['last_activity'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')

                # Log the user in
                login(request, user)

                # Redirect to the appropriate page (e.g., user's statement)
                return redirect('statement')  
        except Exception as e:
            # Handle exceptions here, e.g., log the exception
            traceback.print_exc()

    # Handle GET requests (display login form)
    return render(request, 'users/login.html')



    

def logout_view(request):
    # Log the user out
    logout(request)

    
    return redirect('logout')  

@login_required() 
def statement(request):
    if request.method == "POST":
        form = StatementForm(request.POST)
        if form.is_valid():
            # Process the form data here
            statement = form.cleaned_data['statement']
            originator = form.cleaned_data['originator']
            source = form.cleaned_data['source']
            statement_date = form.cleaned_data['statement_date']
            
            # Perform further processing or save the data to a database
            
            # Redirect to a success page or another view
            return redirect('success_page')
    else:
        form = StatementForm()
    
    return render(request, 'users/statement.html', {'form': form})