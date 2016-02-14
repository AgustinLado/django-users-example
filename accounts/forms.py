from django import forms
from django.contrib.auth.models import User
from django_countries import countries
from django_countries.fields import LazyTypedChoiceField
from django_countries.widgets import CountrySelectWidget

from accounts.fields import phone_regex_validator


class UserProfileForm(forms.ModelForm):
    phone = forms.CharField(max_length=40, required=False,
                            validators=[phone_regex_validator])
    country = LazyTypedChoiceField(choices=countries,
                                   widget=CountrySelectWidget)
    published = forms.BooleanField()

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        # Set the initial values
        self.fields['phone'].initial = kwargs['instance'].profile.phone
        self.fields['country'].initial = kwargs['instance'].profile.country
        self.fields['published'].initial = kwargs['instance'].profile.published

    def save(self, commit=True):
        """
        Save the User instance with its profile info.
        """
        # Save the user
        user = self.instance
        user.save()

        # By this point the User's UserProfile was created. Update it.
        user.profile.phone = self.cleaned_data['phone']
        user.profile.country = self.cleaned_data['country']
        user.profile.published = self.cleaned_data['published']
        user.profile.save()

        return user

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')
