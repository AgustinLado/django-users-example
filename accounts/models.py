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

    def __unicode__(self):
        return u"User {}'s profile".format(self.user.username)


@receiver(models.signals.post_save, sender=User)
def create_user_profile(sender, instance=None, created=False, **kwargs):
    if created:
        UserProfile.objects.get_or_create(user=instance)
