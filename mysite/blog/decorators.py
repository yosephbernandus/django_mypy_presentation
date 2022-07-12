from functools import wraps
from typing import Callable, Any
from django.http import HttpRequest, HttpResponse


def superuser_required(view_func: Callable) -> Callable:
    def _check_superuser(request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        return view_func(request, *args, **kwargs)
    return wraps(view_func)(_check_superuser)
