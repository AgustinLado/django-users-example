import hashlib

from django.contrib.auth.models import User
from django.db import models
from django.dispatch import receiver
from django_countries.fields import CountryField

from accounts.fields import PhoneField


class UserProfile(models.Model):
    """
    Extends the default user model with extra information
    as a one to one relationship.
    """
    user = models.OneToOneField(User, related_name='profile')

    # CharField with custom validation
    phone = PhoneField(blank=True, null=True)

    # CharField with max_length=2 and choices corresponding to ISO 3166-1
    country = CountryField(blank=True, null=True)

    def gravatar(self, size=None):
        """ Get the User's Gravatar url based on his e-mail."""
        return get_gravatar_url(self.user.email, size)

    def __unicode__(self):
        return u"User {}'s profile".format(self.user.username)


@receiver(models.signals.post_save, sender=User)
def create_user_profile(sender, instance=None, created=False, **kwargs):
    if created:
        UserProfile.objects.get_or_create(user=instance)


# Gravatar helper method
GRAVATAR_URL = 'http://www.gravatar.com/avatar/{hash}'


def get_gravatar_url(email, size=None):
    """
    Returns the Gravatar URL linked to the requested email.
    If the User's email isn't linked with Gravatar
    Gravatar's default image is returned.
    The default size is 80x80px.
    """
    url = GRAVATAR_URL.format(
        hash=hashlib.md5(email.lower().strip()).hexdigest()
    )
    if size:
        url += '?s={0}'.format(size)
    return url
