from django.contrib.auth.models import AbstractUser
from activity_log.models import UserMixin


# Only for LAST_ACTIVITY = True
class User(AbstractUser, UserMixin):
    pass

