import hashlib

from django import template

register = template.Library()

GRAVATAR_URL = 'http://www.gravatar.com/avatar/{hash}'


@register.filter
def gravatar_url(email, size=None):
    url = GRAVATAR_URL.format(hash=hashlib.md5(email.lower()).hexdigest())
    if size:
        url += '?s={0}'.format(size)
    return url
