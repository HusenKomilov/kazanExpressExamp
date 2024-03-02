from django.contrib.auth.models import AbstractUser
from django.db.models import CharField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.db import models
from utils.models import BaseModel
from users.managers import UserManger


class Role(BaseModel):
    title = models.CharField(max_length=128)

    def __str__(self):
        return self.title


class User(AbstractUser):
    email = models.EmailField(max_length=256, unique=True)
    first_name = models.CharField(max_length=256)  # type: ignore
    last_name = models.CharField(max_length=256)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_joined = models.DateTimeField(auto_now=True)

    role = models.ManyToManyField(Role, related_name='role')
    image = models.ImageField(upload_to="user/")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['first_name', 'last_name']
    objects = UserManger()

    def tokens(self):
        pass

    def get_absolute_url(self) -> str:
        """Get URL for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})


class OneTimePassword(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=6, unique=True)

    def __str__(self):
        return self.user.email

