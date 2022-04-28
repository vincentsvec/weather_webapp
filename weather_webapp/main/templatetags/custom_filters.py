from django import template
import datetime
import pytz

register = template.Library()


@register.filter
def unix_to_hour(unix, timezone):
    timezone = pytz.timezone(timezone)
    now = datetime.datetime.fromtimestamp(unix, timezone)

    return now.hour


@register.filter
def unix_to_hour_min(unix, timezone):
    timezone = pytz.timezone(timezone)
    now = datetime.datetime.fromtimestamp(unix, timezone)
    now = "{:d}:{:02d}".format(now.hour, now.minute)

    return now


@register.filter
def get_day(unix, timezone):
    timezone = pytz.timezone(timezone)
    now = datetime.datetime.fromtimestamp(unix, timezone)
    index = now.weekday()

    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    day = days[index]

    return day
