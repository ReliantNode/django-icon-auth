from django.contrib.auth import get_user_model, backends
from iconauth.utils import recover_to_addr

class IconAuthBackend(backends.ModelBackend):
    def authenticate(self, request, address=None, token=None, signature=None):
        User = get_user_model()
        addr = recover_to_addr(token, signature)
        if addr == address:
            user, created = User.objects.get_or_create(username=address)
            return user

        return None

    def get_user(self, user_id):
        User = get_user_model()
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None