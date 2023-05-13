from django.shortcuts import redirect
from django.urls import reverse

class LoginCheckMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check if user is authenticated and active
        if (request.user.is_authenticated and request.user.is_active) or \
            (request.path in [reverse('login'), reverse('signup'), reverse('index')]) or \
            (request.path.startswith('/admin/')):
            response = self.get_response(request)
        else:
            # Redirect to login page with next parameter to redirect back after login
            login_url = reverse('login')
            next_url = request.get_full_path()
            redirect_url = f'{login_url}?next={next_url}'
            response = redirect(redirect_url)

        return response
