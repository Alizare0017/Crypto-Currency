from  datetime import datetime, timezone
from django.utils import timezone

def get_req_and_kwarg(args: tuple, kwargs: dict, kw: str):
    """
    get the request object from pos-arguments and kw from keyword-arguments from decorated functions.
    if kwargs not provided just the request object will be returned.
    we need this values to set different permissions for different users
    """
    if not kw:
        return args[1], None
    return args[1], kwargs.get(kw)


def permission_validtor(month_exp,request_count,daily_limit,day_exp_end):
    if month_exp > timezone.now():
        if day_exp_end > timezone.now():
            if request_count <= daily_limit:
                return True
            else:
                return False
        else:
            update_day = "update_day"
            return update_day
    return 'Expierd'