from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.db import models
from journal.models import Person
from oauth2_provider.models import AbstractApplication


class UserManager(BaseUserManager):
    """
    A custom user manager for emr
    """
    def create_user(
            self, first_name=None, last_name=None, email=None, password=None,
            **extra_fields):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            first_name=first_name, last_name=last_name,
            email=self.normalize_email(email),
            **extra_fields)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, first_name=None, last_name=None, email=None,
                         password=None, **extra_fields):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        user = self.create_user(
            first_name,
            last_name,
            email=email,
            password=password,
            **extra_fields
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    """
    A custom user manager for madeasy user
    """

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(verbose_name='email address',
                              max_length=255, unique=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    # used to determine if a user should change their password
    # on during login.
    is_initial = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']


class UserProfile(models.Model):
    """
    This model joins a user to a person

    """
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    person = models.ForeignKey(Person, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return '{} : {}'.format(self.user, self.person)


class OauthApplication(AbstractApplication):
    """
    Oauth aplication table
    Create an end point for registered OAUTH applications
    """
    def __str__(self):
        return self.name or self.client_id

    class Meta(object):
        verbose_name = 'diabetescheck oauth application'
