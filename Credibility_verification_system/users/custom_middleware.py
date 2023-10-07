# custom_middleware.py

from datetime import datetime, timedelta
from django.contrib.auth import logout
from django.conf import settings
from django.shortcuts import redirect

class SessionTimerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            # Get the session's timer value (in seconds) from settings.
            session_timer = getattr(settings, 'SESSION_TIMER', None)

            if session_timer:
                # Check if the user's session has a 'last_activity' timestamp.
                last_activity = request.session.get('last_activity')

                if last_activity:
                    last_activity_time = datetime.strptime(last_activity, '%Y-%m-%d %H:%M:%S.%f')
                    current_time = datetime.now()

                    # Calculate the time elapsed since the last activity.
                    time_elapsed = (current_time - last_activity_time).total_seconds()

                    if time_elapsed > session_timer:
                        # If the timer has expired, log the user out and redirect.
                        logout(request)
                        return redirect('logout') 

            # Update the 'last_activity' timestamp in the user's session.
            request.session['last_activity'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')

        response = self.get_response(request)
        return response
