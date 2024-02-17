import random
import string
from django.core.mail import send_mail
from django.conf import settings
from django.utils import timezone
from datetime import timedelta
from django.shortcuts import redirect

def generate_otp(request, length=6):
    characters = string.digits
    otp = ''.join(random.choice(characters) for _ in range(length))

    # Store the OTP and the current time in the session
    request.session['otp'] = otp
    request.session['otp_time'] = str(timezone.now())

    return otp

# utils.py
def check_otp(request, otp):
    # Check if the OTP is in the session
    if 'otp' in request.session and 'otp_time' in request.session:
        otp_time = timezone.datetime.strptime(request.session['otp_time'], "%Y-%m-%d %H:%M:%S.%f%z")

        # Check if the OTP is correct and if the current time is within 5 minutes from the OTP time
        if request.session['otp'] == otp:
            if timezone.now() - otp_time < timedelta(minutes=5):
                return 'valid'
            else:
                return 'expired'

    return 'invalid'

def send_otp_email(email, otp):
    subject = 'OTP Requested'
    message = f'use {otp} as your one time password to login'
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, from_email, recipient_list)