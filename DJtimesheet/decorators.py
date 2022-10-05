from django.core.exceptions import PermissionDenied
from users.models import CustomUser


def external_required(function):
    def wrap(request, *args, **kwargs):
        user = CustomUser.cus_user.get(pk=kwargs['UserID'])
        if user.Userrole == 'External User':
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied

    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap


def internal_required(function):
    def wrap(request, *args, **kwargs):
        user = CustomUser.cus_user.get(pk=kwargs['UserID'])
        if user.Userrole == 'Internal User':
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied

    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap
