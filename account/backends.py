from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from .models import User

UserModel = get_user_model()


class UserBackend(object):

    def authenticate(self, email, password):
        try:
            user = UserModel.objects.get(email=email)
            if user.check_password(password):  # check valid password
                return user  # return user to be authenticated
        except User.DoesNotExist:  # no matching user exists
            return None

    def get_user(self, user_id):
        try:
            return UserModel.objects.get(pk=user_id)
        except UserModel.DoesNotExist:
            return None