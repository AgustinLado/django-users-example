from django.contrib.auth.views import login as django_login
from django.http import HttpResponseRedirect


def login(request, *args, **kwargs):
    if request.method == 'GET' and request.user.is_authenticated():
        redirect_to = request.GET.get('next', '/')
        return HttpResponseRedirect(redirect_to)
    return django_login(request, *args, **kwargs)
