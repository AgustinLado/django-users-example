from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import login as django_login
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.views import generic

from accounts import forms


def login(request, *args, **kwargs):
    if request.method == 'GET' and request.user.is_authenticated():
        redirect_to = request.GET.get('next', '/')
        return HttpResponseRedirect(redirect_to)
    return django_login(request, *args, **kwargs)


class RegisterView(generic.CreateView):
    template_name = 'accounts/registration_form.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('user-profile')


class UserList(generic.ListView):
    model = User
    template_name = 'accounts/user_list.html'


class UserDetail(LoginRequiredMixin, generic.DetailView):
    model = User
    template_name = 'accounts/user_profile.html'

    def get_object(self, queryset=None):
        """ Overriding get_object allows for calling the view without a PK. """
        return self.request.user


class UserEdit(LoginRequiredMixin, generic.UpdateView):
    model = User
    form_class = forms.UserProfileForm
    template_name = 'accounts/user_update.html'
    success_url = reverse_lazy('user-profile')

    def get_object(self, queryset=None):
        """ Overriding get_object allows for calling the view without a PK. """
        return self.request.user
