from django.conf import settings
from django.http import HttpResponseServerError


class SessionPersistenceMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.path.startswith(("/api/docs", "/auth/token")):
            session_cookie = request.COOKIES.get('sessionid')
            if session_cookie:
                server_number = hash(session_cookie) % getattr(settings, 'NUM_SERVERS', 1)
                request.META['X-Server-Number'] = str(server_number)

            response = self.get_response(request)
            if not session_cookie and response.status_code == 200:
                return HttpResponseServerError("Session cookie is missing.")

            return response

        return self.get_response(request)
