from django.core.validators import RegexValidator
from django.db.models import fields

# Validate the phone field
phone_regex_validator = RegexValidator(
    regex=r'^\+?1?\d{9,15}$',
    message="Phone number must be entered in the format: '+999999999'. "
            "Up to 15 digits allowed."
)


class PhoneField(fields.CharField):
    """
    CharField with custom validation that adheres to the standard described
    here:
      https://www.twilio.com/help/faq/phone-numbers/how-do-i-format-phone-numbers-to-work-internationally
    """
    default_validators = [phone_regex_validator]

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 15
        super(PhoneField, self).__init__(*args, **kwargs)
