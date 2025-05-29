from django.db import transaction
from django.urls import resolve


class AllauthAtomicMiddleware:
    """
    middelware for making allauth request atomic in nature
    (either db saves all data or no data is saved).
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            match = resolve(request.path_info)
        except Exception:
            return self.get_response(request)

        view_func = match.func
    
        if view_func.__module__.startswith("allauth."):
            with transaction.atomic():
                return self.get_response(request)
        else:
            return self.get_response(request)
