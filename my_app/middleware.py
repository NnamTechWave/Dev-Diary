# my_app/middleware.py
from django.shortcuts import redirect

class AdminRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith('/admin/') and not request.user.is_superuser:
            return redirect('admin_login')  # Redirect to admin login if not an admin

        response = self.get_response(request)
        return response
