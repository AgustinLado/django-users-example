from django.contrib.auth.models import User
from django.contrib.auth.views import login as django_login
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.views import generic

from accounts import forms


def login(request, *args, **kwargs):
    if request.method == 'GET' and request.user.is_authenticated():
        redirect_to = request.GET.get('next', '/')
        return HttpResponseRedirect(redirect_to)
    return django_login(request, *args, **kwargs)


class UserDetail(generic.DetailView):
    model = User
    template_name = 'accounts/user_detail.html'

    def get_object(self, queryset=None):
        """ Overriding get_object allows for calling the view without a PK. """
        return self.request.user


class UserEdit(generic.UpdateView):
    model = User
    form_class = forms.UserAccountForm
    template_name = 'accounts/user_update.html'

    def get_object(self, queryset=None):
        """ Overriding get_object allows for calling the view without a PK. """
        return self.request.user

    def get_success_url(self):
        return reverse('home')
