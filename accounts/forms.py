from django import forms
from django.contrib.auth.models import User
from django_countries import countries
from django_countries.fields import LazyTypedChoiceField
from django_countries.widgets import CountrySelectWidget


class UserProfileForm(forms.ModelForm):
    phone = forms.CharField(max_length=40, required=False)
    country = LazyTypedChoiceField(choices=countries,
                                   widget=CountrySelectWidget)

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        # Set the initial values
        self.fields['phone'].initial = kwargs['instance'].profile.phone
        self.fields['country'].initial = kwargs['instance'].profile.country

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
        user.profile.save()

        return user

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')
