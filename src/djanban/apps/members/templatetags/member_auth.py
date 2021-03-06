from django import template

from djanban.apps.base import auth

register = template.Library()


@register.filter
def user_is_administrator(user):
    """
    Template filter that checks if the user is an
    Parameters
    ----------
    user: auth.User that will be checked.

    Returns
    -------
    True if the user is an administrator, False otherwise.
    """
    return auth.user_is_administrator(user)