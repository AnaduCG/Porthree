from django.shortcuts import redirect
from django.urls import reverse
from django.utils import timezone
from django.conf import settings

class SessionTimeoutMiddleware:
    """
    managed timed authentication
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            last_activity_str = request.session.get('last_activity')

            # Check if last_activity_str is not None
            if last_activity_str is not None:
                # Convert string back to datetime
                last_activity = timezone.datetime.fromisoformat(last_activity_str)

                # Convert datetime to timestamp for session storage
                session_timeout_timestamp = (timezone.now() - last_activity).total_seconds()

                if session_timeout_timestamp > settings.SESSION_COOKIE_AGE:
                    # Session expired, log the user out
                    del request.session['last_activity']

        response = self.get_response(request)

        # Save the datetime as a string in ISO 8601 format
        request.session['last_activity'] = timezone.now().isoformat()

        return response
