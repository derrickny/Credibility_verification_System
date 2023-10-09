from django.shortcuts import render, redirect
from .forms import UserForm, StatementForm, EditProfileForm,PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from datetime import datetime
from django.contrib.auth import authenticate, login, update_session_auth_hash
import traceback
from django.contrib import messages 

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


@login_required
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

            # For example, you can create a Statement model and save the data:
            # statement_obj = Statement(
            #     statement=statement,
            #     originator=originator,
            #     source=source,
            #     statement_date=statement_date,
            #     user=request.user  # If you have a ForeignKey to User
            # )
            # statement_obj.save()

            # Redirect to a success page or another view
            messages.success(request, 'Statement submitted successfully!')
            return redirect('success_page')  # Change 'success_page' to your desired URL name

    else:
        form = StatementForm()
    
    return render(request, 'users/statement.html', {'form': form})


@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()

            # Add a success message
            messages.success(request, 'Your credentials have been changed successfully.')

            return redirect('statement')  # Redirect to the user's profile page
    else:
        form = EditProfileForm(instance=request.user)

    return render(request, 'users/edit_profile.html', {'form': form})


@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important for keeping the user logged in
            return redirect('edit_profile')  # Redirect to the user's profile page after password change
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'users/password.html', {'form': form})