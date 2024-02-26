from django.contrib.auth.models import AbstractUser
from django.db.models import CharField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.db import models
from utils.models import BaseModel


class Role(BaseModel):
    title = models.CharField(max_length=128)

    def __str__(self):
        return self.title


class User(AbstractUser):
    # class Role(models.TextChoices):
    #     SHOP_ADMIN = "shop"
    """
    Default custom user model for My Awesome Project.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """

    # First and last name do not cover name patterns around the globe
    name = CharField(_("Name of User"), blank=True, max_length=255)
    first_name = None  # type: ignore
    last_name = None  # type: ignore
    # # role = models.CharField(max_length=128, choices=choices.Role.choices)
    role = models.ManyToManyField(Role, related_name='role')

    # is_product_admin = models.BooleanField(default=False)
    # is_shop_admin = models.BooleanField(default=False)
    # is_categorry_ad
    def get_absolute_url(self) -> str:
        """Get URL for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})
