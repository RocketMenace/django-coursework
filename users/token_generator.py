from django.contrib.auth.tokens import PasswordResetTokenGenerator

class  VerificationToken(PasswordResetTokenGenerator):

    def _make_hash_value(self, user, timestamp):
        return user.is_active + user.pk + timestamp

verification_token = VerificationToken()