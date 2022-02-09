#-------------Note----------------

#PasswordRestTokenGenerator - generate token without persisting it in the database
#Once user clicked the register link the default value for the password_reset_tomeout_dat is 7


from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils import six
from six import text_type

class AccountActivationTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (
            six.text_type(user.pk) + six.text_type(timestamp) +
            six.text_type(user.profile.signup_confirmation)
        )

account_activation_token = AccountActivationTokenGenerator()

