from django.shortcuts import render, redirect
from .forms import UserForm, StatementForm, EditProfileForm,PasswordChangeForm,OTPForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from datetime import datetime
from django.contrib.auth import authenticate, login, update_session_auth_hash
import traceback
from django.contrib import messages 
from .utils import generate_otp, send_otp_email  
# Your Django view function here


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



def login_view(request):
    if request.method == 'POST':
        try:
            username = request.POST['username']
            password = request.POST['password']

            # Authenticate the user
            user = authenticate(request, username=username, password=password)

            if user is not None:
                # Store the username and last_activity timestamp in the session
                request.session['username'] = username
                request.session['last_activity'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')

                # Generate an OTP
                otp = generate_otp()

                # Send the OTP to the user's email
                send_otp_email(user.email, otp)  # Replace 'user.email' with the actual user email field

                # Store the OTP in the session
                request.session['otp'] = otp

                # Log in the user
                login(request, user)

                # Redirect to the OTP verification page
                return redirect('verify_otp')
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
    # Check if the user has a verified OTP

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



@login_required
def verify_otp(request):
    error_message = None  # Initialize error message as None
    success_message = None  # Initialize success message as None

    if request.method == 'POST':
        # Get the entered OTP from the form
        form = OTPForm(request.POST)
        if form.is_valid():
            entered_otp = form.cleaned_data['otp']

            # Get the stored OTP from the user's session
            stored_otp = request.user.otp

            if entered_otp == stored_otp:
                # OTP is valid, allow the user to access statements
                del request.user.otp  # Remove OTP from the user's model
                return redirect('statement')  # Redirect to the statements view
            else:
                # OTP is invalid, set the error_message
                error_message = 'The OTP you entered is incorrect. Please check your email for the latest OTP.'
    else:
        # Generate and send a new OTP when the page is initially loaded
        otp = generate_otp()
        send_otp_email(request.user.email, otp)  # Replace 'request.user.email' with the actual user email field
        request.user.otp = otp
        request.user.save()

        # Set the success_message for OTP sent
        success_message = f'Success! An OTP code has been sent to your Email {hide_email(request.user.email)}.'

    # Display OTP verification form
    form = OTPForm()

    # Handle the "Back to login" action
    if 'back_to_login' in request.POST:
        logout(request)  # Log the user out
        return redirect('login')  # Redirect to the login page

    return render(request, 'users/verify_otp.html', {'form': form, 'error_message': error_message, 'success_message': success_message})

def hide_email(email):
    # Helper function to hide part of the email address
    parts = email.split('@')
    return f'{parts[0][:3]}***@{parts[1]}'  # Display part of the email