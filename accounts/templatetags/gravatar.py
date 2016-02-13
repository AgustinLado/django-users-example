from django import template

from accounts.models import get_gravatar_url

register = template.Library()


@register.filter
def gravatar_url(email, size=None):
    """
    Using a template filter allows the passing of the size parameter
    in the template language.
    """
    return get_gravatar_url(email, size)
