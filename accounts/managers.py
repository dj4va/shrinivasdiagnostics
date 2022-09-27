from django.contrib.auth.base_user import BaseUserManager
from django.utils import timezone
from django.contrib.contenttypes.models import ContentType

from datetime import datetime


class UserManager(BaseUserManager):
    use_in_migrations = True

    # def _create_user(self, email, password, **extra_fields):
    def _create_user(self, email, password, is_staff, is_superuser, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        now = timezone.now()
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        # user = self.model(email=email, **extra_fields)
        user = self.model(email=email, is_staff=False, is_active=True, is_superuser=False, last_login=now, date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_user(self, email, password=None, **extra_fields):
        # extra_fields.setdefault('is_superuser', False)
        # return self._create_user(email, password, **extra_fields)
        return self._create_user(email, password, False, False, **extra_fields)


    def create_superuser(self, email, password, **kwargs):
        # user = self.model(email=email, is_staff=True, is_admin=True, is_superuser=True, is_active=True, **kwargs)
        user = self.model(email=email, is_staff=True, is_superuser=True, is_active=True, **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user
