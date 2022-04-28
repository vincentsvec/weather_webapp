"""
Custom context
"""
from .models import User_data


def get_unit(request):
    if str(request.user) != "AnonymousUser":
        unit = request.user.user_data.first().weather_unit
        return {"unit": unit}

    else:
        return {"unit": "metric"}
